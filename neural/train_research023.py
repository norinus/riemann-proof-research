"""Tiny premise-ranking experiment. Never marks a statement as proved."""
import hashlib
import json
from pathlib import Path
import re
import torch
from neural.model import ProofRanker, train_step


def vector(claim):
    v = torch.zeros(64)
    for token in re.findall(r'[a-z0-9]+',claim.lower()):
        i = int.from_bytes(hashlib.sha256(token.encode()).digest()[:4],'big') % 64
        v[i] += 1
    return v / v.norm().clamp_min(1)


def sample(nodes, goal_id, excluded=()):
    # Use preceding nodes only, including no target incident edges or open nodes.
    i = next(i for i,n in enumerate(nodes) if n['id']==goal_id)
    goal = nodes[i]
    pool = [n for n in nodes[:i] if n['status']!='open' and n['id'] not in excluded]
    ids = {n['id']:j for j,n in enumerate(pool)}
    assert set(goal['deps']) <= ids.keys()
    pairs = [(ids[d],ids[n['id']]) for n in pool for d in n['deps'] if d in ids]
    edges = torch.tensor(pairs,dtype=torch.long).reshape(-1,2).T.contiguous()
    labels = torch.tensor([int(n['id'] in goal['deps']) for n in pool])
    return torch.stack([vector(n['claim']) for n in pool]),edges,vector(goal['claim']),labels


def run():
    data = json.loads((Path(__file__).resolve().parents[1]/'data/research023-dependencies.json').read_text())
    nodes = data['nodes']
    seen = set()
    for n in nodes:
        assert n['id'] not in seen and set(n['deps']) <= seen
        seen.add(n['id'])
    torch.manual_seed(23)
    torch.set_num_threads(1)
    torch.use_deterministic_algorithms(True)
    model = ProofRanker(hidden=32)
    opt = torch.optim.Adam(model.parameters(),lr=.01)
    samples = [sample(nodes,g,{data['holdout_goal']}) for g in data['train_goals']]
    held = sample(nodes,data['holdout_goal'])
    def loss_all():
        with torch.no_grad():
            return sum(torch.nn.functional.binary_cross_entropy_with_logits(model(x,e,g),y.float()).item() for x,e,g,y in samples)/len(samples)
    before = loss_all()
    for _ in range(40):
        for args in samples:
            train_step(model,opt,*args)
    after = loss_all()
    x,e,g,y = held
    with torch.no_grad():
        rank = model(x,e,g).argsort(descending=True)
        k = int(y.sum())
        hits = int(y[rank[:k]].sum())
    assert after < before
    return {'nodes':len(nodes),'training_goals':len(samples),'steps':40*len(samples),'loss_before':before,'loss_after':after,'heldout_hits_at_k':hits,'k':k,'torch':str(torch.__version__)}


if __name__ == '__main__':
    print(json.dumps(run(),sort_keys=True))

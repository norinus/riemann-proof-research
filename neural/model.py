import torch
from torch import nn

class ProofRanker(nn.Module):
    """Message-passing graph encoder and goal-conditioned premise scorer."""
    def __init__(self, features=64, hidden=128):
        super().__init__()
        self.embed = nn.Linear(features, hidden)
        self.layers = nn.ModuleList(nn.Linear(2*hidden, hidden) for _ in range(3))
        self.goal = nn.Linear(features, hidden)
        self.score = nn.Linear(2*hidden, 1)

    def forward(self, nodes, edges, goal):
        h = self.embed(nodes).relu()
        src, dst = edges
        for layer in self.layers:
            agg = torch.zeros_like(h).index_add_(0, dst, h[src])
            degree = h.new_zeros(h.size(0)).index_add_(0, dst, h.new_ones(dst.numel()))
            h = layer(torch.cat((h, agg / degree.clamp_min(1).unsqueeze(1)), dim=1)).relu()
        g = self.goal(goal).expand_as(h)
        return self.score(torch.cat((h,g),dim=1)).squeeze(-1)

def train_step(model, optimizer, nodes, edges, goal, labels):
    optimizer.zero_grad()
    loss = nn.functional.binary_cross_entropy_with_logits(model(nodes, edges, goal), labels.float())
    loss.backward()
    optimizer.step()
    return loss.item()

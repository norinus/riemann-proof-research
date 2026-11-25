import unittest
import torch
from neural.model import ProofRanker, train_step

class ModelTest(unittest.TestCase):
    def test_training_smoke(self):
        model = ProofRanker()
        x = torch.randn(4,64)
        edges = torch.tensor([[0,1,2],[1,2,3]])
        goal = torch.randn(64)
        self.assertEqual(tuple(model(x,edges,goal).shape),(4,))
        loss = train_step(model,torch.optim.Adam(model.parameters()),x,edges,goal,torch.tensor([0,1,0,1]))
        self.assertTrue(torch.isfinite(torch.tensor(loss)))

if __name__ == "__main__":
    unittest.main()

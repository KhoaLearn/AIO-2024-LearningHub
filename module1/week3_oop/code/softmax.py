import torch
import torch.nn as nn

class Softmax(nn.Module):
    def __init__(self):
        super(Softmax, self).__init__()

    def forward(self, x):
        exp_x = torch.exp(x)
        return exp_x / exp_x.sum(dim=0)

class SoftmaxStable(nn.Module):
    def __init__(self):
        super(SoftmaxStable, self).__init__()

    def forward(self, x):
        c = x.max()
        exp_x = torch.exp(x - c)
        return exp_x / exp_x.sum(dim=0)

# Examples
data = torch.Tensor([1, 2, 3])

# Using the Softmax class
softmax = Softmax()
output = softmax(data)
print(output)  # Expected: tensor([0.0900, 0.2447, 0.6652])

# Using the SoftmaxStable class
softmax_stable = SoftmaxStable()
output_stable = softmax_stable(data)
print(output_stable)  # Expected: tensor([0.0900, 0.2447, 0.6652])

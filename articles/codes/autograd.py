import torch
from torch.autograd import grad
import torch.nn.functional as F

# Neuron
x = torch.tensor([3.])
w = torch.tensor([2.],requires_grad=True)
b = torch.tensor([1.],requires_grad=True)
a = F.relu(x*w+b)
print(a)
#> tensor([7.],grad_fn=<ReluBackward0>)

# Derivate partial in w
print(grad(a,w,retain_graph=True))
#> (tensor([3.]),)

# Construct your own ativaction function
def my_relu(z):
    if z>0.:
        return z
    else: 
        z[:] = 0.
        return z

a = my_relu(x*w+b)
print(grad(a,w))
#> (tensor([3.]),)
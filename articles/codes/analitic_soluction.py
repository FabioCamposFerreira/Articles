# Analytical Solution

# Libraries
from multiprocessing import current_process
import pandas as pd             # used to open csv files
import matplotlib.pyplot as plt # used
import torch                    # used manipule vectors

#===============================
# Making DataBase
#===============================

# Creating two classes with two features. 150 features vectors in total
x1 = 
x2 = 
y = 
data_frame = pd.

# Creating x and y vectors using torch
X = torch.tensor(data_frame[["x1","x2"].values,dtype=torch.float])
y = torch.tensor(data_frame["y"].values,dtype=torch.float)

# Shuffling & train/test split
torch.manual_seed(123) # set same shuffling to run many times and get same result
shuffle_index = torch.randperm(y.size(0),dtype=torch.long)
X,y = X[shuffle_index], y[shuffle_index]

# Train
xb = torch.cat((torch.ones((X.size(0),1)),X),dim=1) # vector x + bias
w = torch.zeros(X.size(1))                          # weights vector empy 
z=torch.inverse(torch.matmul(xb.t(),xb))            # z = (X^T*X)^(-1)
params = torch.matmul(z,torch.matmul(xb.t(),y))     # params = z*X^T*y
b, w = torch.tensor([params[0]]),params[1:].view(X.size(1),1)

# Show results
print("Analytical weights",w)
print("Analytical bias",b)


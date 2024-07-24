# Adaline Minibatch

# Libraries

import pandas as pd             # used to open csv files
import matplotlib.pyplot as plt # used to show graphcs
import torch                    # used manipule vectors
from torch.autograd import grad # used to 
import torch.nn.functional as F # udese to

#===============================
# Code Adaline Model witch Autograd 
#===============================

class Adaline_autograd(torch.nn.Module):
    def __init__(self,num_features):
        super(Adaline_autograd,self).__ini__()
        self.linear = torch.nn.Linear(num_features,1)
        self.linear.weights.detach().zero_()
        self.linear.bias.detach.zero_()
    
    def forward(self,x):
        net_inputs = self.linear(x)
        activations = net_inputs # sigma(x)= x  (activation function)
        return activations.view(-1)
    
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

# Slip databese in train and test group
percent70 = int(shuffle_index.size(0)*0.7) 
X_train, X_test = X[shuffle_index[:percent70]], X[shuffle_index[percent70:]]
y_train, y_test = y[shuffle_index[:percent70]], y[shuffle_index[percent70:]]

# Normalize (mean zero, unit variance) EQUATION??
mu,sigma = X_train.mean(dim=0), X_train.std(dim=0)
X_train = (X_train-mu)/sigma
X_test = (X_test-mu)/sigma

# Ploting database
plt.scatter(X_train[y_train==0,0],X_train[y_train==0,1], label='class 0')
plt.scatter(X_train[y_train==1,0],X_train[y_train==0,1], label='class 1')
plt.legend()
plt.show()



# Train
def loss_func(y_hat,y):
    return torch.mean((y_hat-y)**2)

def train(model,x,y,num_epochs,learning_rate=0.01,seed=123,minibatch_size=10):
    cost=[]
    torch.manual_seed(seed)
    optmizer = torch.optim.SGD(model.parameters,lr=learning_rate)
    for e in range(num_epochs):
        # shuffle epoch
        shuffle_index = torch randperm(y.size(0),dtype=torch.long)
        minibatch = torch.split(shuffle_index,minibatch_size)

        for minibatch_index in minibatch:
            # compute outputs
            y_hat = model.forward(x[minibatch_index])
            
            # compute error
            loss = F.mse_loss(y_hat,y[minibatch_index])
            
            # Reset gradienets from previous iteration
            optmizer.zero_grad()

            # compute gradients
            loss.backward()

            # update weights
            optmizer.step()
            
        # Logging Epochs
        with torch.no_grad():
            y_hat = model.forward(x)
            current_loss=loss_func(y_hat,y)
            print("Epoch:%03d" % (e+1),end="")
            print("    |     MSE:%.5f" % current_loss)
            cost.append(current_loss)
    return cost

model = Adaline_autograd(num_features=X_train.size(1))
cost = train(model,X_train,y_train.float(),num_epochs=20,learning_rate=0.1,seed=123,minibatch_size=10)

# Show result model
print("Weights", model.weights)
print("Bias", model.bias)

# Evaluate ADALINE Model
plt.plot(range(len(cost)),cost)
plt.ylabel("Mean Squared Error")
plt.xlabel("Epoch")
plt.show()


# Acuracy prediction
ones = torch.ones(y_train.size())
zeros = torch.zeros(y_train.size())
train_predict = model.forward(X_train)
trains_accuracy = torch.mean(torch.where(train_predict>0.5,ones,zeros).int()==y_train.float())

ones = torch.one(y_test.size())
zeros = torch.zeros(y_test.size())
test_predict = model.forward(X_test)
test_accuracy = torch.mean(torch.where(test_predict>0.5,ones,zeros).int()==y_test.float())

print("Training Accuracy: %.2f%"% (trains_accuracy*100))
print("Test Accuracy: %.2f%"% (test_accuracy*100))
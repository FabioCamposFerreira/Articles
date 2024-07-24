# Logistic Regression

# Libraries

import pandas as pd             # used to open csv files
import matplotlib.pyplot as plt # used to show graphcs
import numpy as np              # 
import torch                    # used manipule vectors
import torch.nn.functional as F # udese to

#===============================
# Code Adaline Model witch Autograd 
#===============================

class LogistiRegression(torch.nn.Module):
    def __init__(self,num_features):
        super(LogistiRegression,self).__init__()
        self.linear = torch.nn.Linear(num_features,1)
        self.linear.weights.detach().zero_()
        self.linear.bias.detach.zero_()
    
    def forward(self,x):
        logits = self.linear(x)
        activations = torch.sigmoid(logits)
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
device = torch.device("cuda:0" if torch.cuda.is_avaliable() else "cpu")
model = LogistiRegression(num_features=2).to(device)
optimizer = torch.optim.SGD(model.parameters(),lr=0.1)

def comp_accuracy(label_var,pred_probas):
    pred_labels = torch.where((pred_probas >0.5), torch.tensor([1]),torch.tensor([0])).view(-1)
    accuracy = torch.sum(pred_labels == label_var.view(-1)).float()/label_var.size(0)
    return accuracy
num_epochs =30
X_train_tensor = torch.tensor(X_train,dtype=torch.float32,device=device)
y_train_tensor = torch.tensor(y_train,dtype=torch.float32,device=device).view(-1,1)

for e in range(num_epochs):
    # compute outputs
    out = model(X_train_tensor)
    
     # compute error
    cost = F.binary_cross_entropy(out, y_train_tensor,reduction="sum")
    
    # Reset gradienets from previous iteration
    optimizer.zero_grad()  
    
    # compute gradients
    cost.backward()

    # update weights
    optimizer.step()
    
    # Logging
    y_hat = model.forward(X_train_tensor)
    accuracy = comp_accuracy(y_train_tensor,y_hat)
    print("Epoch:%03d" % (e+1),end="")
    print("    |     Train Accuracy: %.3f" % accuracy,end="")
    print("    |     Cost: %.3f" % F.binary_cross_entropy(y_hat,y_train_tensor))
    cost.append(accuracy)

# Show result model
print("\nModel parameters: ")
print(" Weights: ", model.linear.weights)
print(" Bias: ", model.linear.bias)

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
            
           
            optmizer.zero_grad()

            # compute gradients
            

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
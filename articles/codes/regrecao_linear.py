# Regração Linear

# Libraries
from multiprocessing import current_process
import pandas as pd             # used to open csv files
import matplotlib.pyplot as plt # used
import torch                    # used manipule vectors

#===============================
# Linear Regretion Model
#===============================

class Linear_Regression():
    def __init__(self,num_features):
        self.num_features = num_features
        self.weights = torch.zeros(num_features,1,dtype=torch.float)
        self.bias = torch.zeros(1,dtype=torch.float)
    
    def forward(self,x):
        net_inputs = torch.add(torch.mm(x,self.wights),self.bias) #(x^T*w+b)
        activations = net_inputs # sigma(x)= x  (activation function)
        return activations.view(-1)
    
    def backward(self,x,yhat,y):
        grad_loss_yhat= 2*(yhat-y) #2(sigma(w^T*x)-y)
        grad_yhat_weights = x
        grad_yhat_bias = 1.

        # Chain rule: inner times outer
        grad_loss_weights = torch.mm(grad_yhat_weights.t(),grad_loss_yhat.view(-1,1))/y.size(0) # (grad_loss_yhat*x_j)/media
        grad_loss_bias = torch.sum(grad_yhat_bias*grad_loss_yhat)/y.size(0)

        # return negative gradient
        return (-1)*grad_loss_weights,(-1)*grad_loss_bias




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



# Trein
def loss(y_hat,y):
    return torch.mean((y_hat-y)**2)
    
def train(model,x,y,num_epochs,learning_rate=0.01):
    cost=[]
    for e in range(num_epochs):
        # compute outputs
        y_hat = model.forward(x)
        
        # compute gradients
        negative_gradiente_w,negative_gradiente_b = model.backward(x,y_hat,y)

        # update weights
        model.weights += learning_rate*negative_gradiente_w # w := w+\delta*w
        model.bias += learning_rate*negative_gradiente_b # b := b+\delta*b

        # Logging Epochs
        y_hat = model.forward(x)
        current_loss=loss(y_hat,y)
        print("Epoch:%03d" % (e+1),end="")
        print("    |     MSE:%.5f" % current_loss)
        cost.append(current_loss)
    return cost

model = Linear_Regression(num_features=X_train.size(1))
cost = train(model,X_train,y_train,num_epochs=100,learning_rate=0.05)

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
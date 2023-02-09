#--------------------------
# Perceptron using for loop
x_0, x_1, x_2 = 1,2,3
bias, w_1, w_2 = 0.1,0.3,0.5
x = [x_0, x_1, x_2]
w = [bias, w_1, w_2]
z = 0
for i in range(len(x)):
    z += x[i] * w[i]
print(z)
# 2.2

#------------------------
# Perceptron using vector
import numpy as np
x_0, x_1, x_2 = 1,2,3
bias, w_1, w_2 = 0.1,0.3,0.5
x = [x_0, x_1, x_2]
w = [bias, w_1, w_2]
x_vec, w_vec = np.array(x), np.array(w)
z = x_vec.dot(w_vec)
print(z)
# 2.2

#============================================
# Code full Perceptron
import numpy as np
import bokeh

np.getfromtxt("data_base.txt","\t")

X_train =
X_test =

# Shuffling and slip in train and test
input.shuffle()

# normalization mean zero
mu, sigma = X_train.mean(), X_train.std
X_train = (X_train - mu) / sigma
X_test = (X_test - mu) / sigma

# plot

class Perceptron():
    def __init__(self, num_features):
        """"Contrtruct shape of de vectors weights and variables bias and num_features"""
        self.num_features = num_features
        self.weights = np.zeros((num_features,1), dtype=np.float)
        self.bias = np.zeros(1, dtype=np.float)
    
    def forward(self, x):
        """"Calcula a saida da rede (produti escalar)"""
        linear = np.dot(x,self.weights) + self.bias
        predictions = np.where(linear > 0.,1,0)
        return predictions
    
    def backward(self,x,y):
        """"Calcula o erro"""
        predictions = self.forward(x)
        errors = y - predictions
    
    def train(self,x,y,epochs):
        """Cacula o erro, atualia os pessos"""
        for e in range(epochs):
            for i in range(y.shape[0]):
                errors = self.backward(x[i].reshape(1,self.num_features) ,y[i]).reshape(-1)
                self.weights += (erros* x[i]).reshape(self.num_features,1)
                self.bias += errors
    
    def evaluate(self,x,y):
        """Retorna a acurracia"""
        predictions = self.forward(x).reshape(-1)
        accuracy = np.sum(predictions == y) / y.shape[0]
        return accuracy
    
    ppn = Perceptron(num_features=2)
    ppm.train(X_train, y_train,epochs=5)
    ppm.evaluate(X_test, y_test)

    # Calcular e protrar a região de decisão
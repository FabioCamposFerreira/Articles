# Linear Regression Keras

import numpy as np
import tensorflow as tf

# Creating Data
X, y= [],[]

# Show data
print("Class label counts",np.bincount(y))
print("X.shape: ", x.shape)
print("y.shape: ",y.shape)
print(x[0])
print([y[0]])

# Split data
from sklearn.model_selection import train_test_split
X_train, X_trest, y_train, y_test = train_test_split(X,y,test_size=0.4,random_state=123)
print("x_train.shape: ",x_train.shape)
print("y_train.shape: ",y_train.shape)
print("x_test.shape: ",x_test.shape)
print("y_test.shape: ",y_train.shape)

# Normalization
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler();
scaler.Fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
print("X_train.mean: ",np.mean(X_train))
print("X_train.standard deviation: ",np.std(X_train))

# Creating Linear Regression
model = tf.keras.models.Sequential()
model.add(tf.keras.Input(shape=(2,)))
model.add(tf.keras.layers.Dense(1,kernel_initializer="zeros"))
model.add(tf.keras.layers.activation("linear"))
model.compile(loss="mse", optimizer="sgd", metrics=["mse"])
model.sumary()

# Training
model.fit(X_train,y_train,epochs=10,batch_size=5,verbose=1)

# Evaluation - Accuracy
test_loss,test_accuracy= model.evaluate(X_test,y_test)

# Evaluation - Confusion Matrix
from sklearn.metrics import confusion_matrix
confusion_matrix(y_test_pred, y_test)

 
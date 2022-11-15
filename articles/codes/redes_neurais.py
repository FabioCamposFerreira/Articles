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

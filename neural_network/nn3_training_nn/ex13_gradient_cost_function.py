import sys, os
sys.path.append(os.path.abspath("../"))
import numpy as np
from nn2_neural_network.ex12_softmax import softmax
from ex04_cross_entropy_error_minibatch import cross_entropy_error
from ex08_gradient import numerical_gradient
import pdb
             
class simpleNet:
    def __init__(self):
        self.W = np.random.randn(2,3) 
    def predict(self, x):
        return np.dot(x, self.W)
    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y, t)
        return loss

if __name__=="__main__":
    net = simpleNet()
    x = np.array([0.6, 0.9])
    p = net.predict(x)
    t = np.array([0, 0, 1]) 

    f = lambda w: net.loss(x,t)
    dW = numerical_gradient(f, net.W)
    print(dW)



 

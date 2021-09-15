import sys, os
sys.path.append(os.path.abspath("../"))
import numpy as np
from nn2_neural_network.ex12_softmax import softmax
from ex04_cross_entropy_error_minibatch import cross_entropy_error
from ex08_gradient import numerical_gradient
             
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


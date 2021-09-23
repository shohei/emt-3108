import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.abspath(__file__),"../../")))
sys.path.append(os.path.abspath(os.path.join(os.path.abspath(__file__),"../../../")))
from nn3_training_nn.ex04_cross_entropy_error_minibatch import cross_entropy_error
from nn2_neural_network.ex13_softmax_improved import softmax

class SoftmaxWithLoss:
    def __init__(self):
        self.loss = None # Loss
        self.y = None # softmax output
        self.t = None # Label (one-hot vector)
    def forward(self, x, t):
        self.t = t
        self.y = softmax(x)
        self.loss = cross_entropy_error(self.y, self.t)
        return self.loss
    def backward(self, dout=1):
        batch_size = self.t.shape[0]
        dx = (self.y - self.t) / batch_size
        return dx
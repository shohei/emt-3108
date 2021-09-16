import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.abspath(__file__),"../../")))
sys.path.append(os.path.abspath(os.path.join(os.path.abspath(__file__),"../../../")))
import numpy as np

class Sigmoid:
        def __init__(self):
            self.out = None
        def forward(self, x):
            out = 1 / (1 + np.exp(-x))
            self.out = out
            return out
        def backward(self, dout):
            dx = dout * (1.0 - self.out) * self.out
            return dx


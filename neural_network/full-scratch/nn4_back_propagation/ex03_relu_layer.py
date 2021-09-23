import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.abspath(__file__),"../../")))
sys.path.append(os.path.abspath(os.path.join(os.path.abspath(__file__),"../../../")))
class Relu:
        def __init__(self):
            self.mask = None
        def forward(self, x):
            self.mask = (x <= 0)
            out = x.copy()
            out[self.mask] = 0
            return out
        def backward(self, dout):
            dout[self.mask] = 0
            dx = dout
            return dx

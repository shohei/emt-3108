import numpy as np
import matplotlib.pylab as plt
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.abspath(__file__),"../../")))
sys.path.append(os.path.abspath(os.path.join(os.path.abspath(__file__),"../../../")))

def relu(x):
    return np.maximum(0, x)

if __name__=="__main__":
    x = np.arange(-5.0, 5.0, 0.1)
    y = relu(x)
    plt.plot(x, y)
    plt.show()
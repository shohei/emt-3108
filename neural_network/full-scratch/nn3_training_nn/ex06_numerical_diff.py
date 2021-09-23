import numpy as np
import matplotlib.pylab as plt
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.abspath(__file__),"../../")))
sys.path.append(os.path.abspath(os.path.join(os.path.abspath(__file__),"../../../")))

def numerical_diff(f, x):
    h = 1e-4 # 0.0001
    return (f(x+h) - f(x-h)) / (2*h)

def function_1(x):
    return 0.01*x**2 + 0.1*x

if __name__=="__main__":
    x = np.arange(0.0, 20.0, 0.1) # 0 to 20, by 0.1 division
    y = function_1(x)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.plot(x, y)
    plt.show()

    print(numerical_diff(function_1, 5)) # 0.1999999999990898
    print(numerical_diff(function_1, 10)) # 0.2999999999986347
    
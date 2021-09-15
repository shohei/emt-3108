from mpl_toolkits import mplot3d
import numpy as np
from ex07_partial_diff import function_2
import matplotlib.pyplot as plt
import pdb

def numerical_gradient(f, x):
    h = 1e-4 # 0.0001
    grad = np.zeros_like(x)
    for idx in range(x.size):
        tmp_val = x[idx]
        x[idx] = tmp_val + h 
        fxh1 = f(x)
        x[idx] = tmp_val - h 
        fxh2 = f(x)
        grad[idx] = (fxh1 - fxh2) / (2*h) 
        x[idx] = tmp_val 
    return grad

if __name__=="__main__":
    x1 = np.linspace(-2,2,20)
    x2 = np.linspace(-2,2,20) 
    grads = [[[]]*len(x1)]*len(x2)
    plt.figure(1)
    X, Y = np.meshgrid(x1, x2)
    Z = X**2+Y**2
    ax = plt.axes(projection='3d')
    ax.plot_surface(X,Y,Z,cmap='viridis', edgecolor='none')

    plt.figure(2)
    for i, x1i in enumerate(x1):
        for j, x2j in enumerate(x2):
            grads[i][j] = numerical_gradient(function_2, np.array([x1i, x2j]))
            u = -grads[i][j][0]
            v = -grads[i][j][1]
            plt.quiver(x1i,x2j, u, v, width=0.003)
    plt.show()
from mpl_toolkits import mplot3d
import numpy as np
from ex07_partial_diff import function_2
import matplotlib.pyplot as plt
from ex08_gradient import numerical_gradient

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
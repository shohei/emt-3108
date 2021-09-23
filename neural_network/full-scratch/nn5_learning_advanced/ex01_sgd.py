import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.abspath(__file__),"../../")))
sys.path.append(os.path.abspath(os.path.join(os.path.abspath(__file__),"../../../")))
import numpy as np
import matplotlib.pyplot as plt

class SGD:
    def __init__(self, lr=0.01):
        self.lr = lr
    def update(self, params, grads):
        for key in params.keys():
            params[key] -= self.lr * grads[key]

def f(x,y):
    return x**2 /20.0 + y**2

def df(x,y):
    return x/10.0, 2.0*y

def plot_contour(n1,n2,n3,X,Y,Z):
    plt.subplot(n1,n2,n3)
    plt.contour(X,Y,Z)
    plt.plot(0,0,'+')

def plot_gradient(n1,n2,n3):
    plt.subplot(n1,n2,n3)
    for xi in x[::100]:
        for yj in y[::100]:
            grads['x'], grads['y'] = df(xi,yj)
            u = -grads['x']
            v = -grads['y']
            plt.quiver(xi,yj, u, v, width=0.003)

if __name__=="__main__":
    x = np.arange(-10,10,0.01)
    y = np.arange(-5,5,0.01) 
    init_pos = (-7.0, 2.0)
    params = {}
    grads = {}
    grads['x'], grads['y'] = 0, 0

    plt.figure(1)
    X, Y = np.meshgrid(x, y)
    Z = f(X,Y)
    ax = plt.axes(projection='3d')
    ax.plot_surface(X,Y,Z,cmap='viridis', edgecolor='none')

    plt.figure(2)
    plot_contour(2,1,1,X,Y,Z)

    optimizer = SGD(lr=0.95)
    x_history = []
    y_history = []
    params['x'], params['y'] = init_pos[0], init_pos[1]
    for i in range(30):
        x_history.append(params['x'])
        y_history.append(params['y'])
        grads['x'], grads['y'] = df(params['x'], params['y'])
        optimizer.update(params, grads)

    plot_contour(2,1,2,X,Y,Z)
    plt.plot(x_history, y_history, 'o-', color="red")

    plt.figure(3)
    plot_gradient(2,1,1)

    plot_gradient(2,1,2)
    plt.plot(x_history, y_history, 'o-', color="red")

    plt.show()
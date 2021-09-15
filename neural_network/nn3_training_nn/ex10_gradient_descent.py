import numpy as np
from ex08_gradient import numerical_gradient

def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x  = init_x
    for i in range(step_num):
        grad = numerical_gradient(f, x)
        x -= lr * grad
    return x

def function_2(x):
    return x[0]**2 + x[1]**2 

if __name__=="__main__":
    init_x = np.array([-3.0, 4.0]) 
    print(gradient_descent(function_2, init_x=init_x, lr=0.1, step_num=100)) #array([ -6.11110793e-10, 8.14814391e-10]) 
 
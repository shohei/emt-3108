import numpy as np

def numerical_diff(f, x):
    h = 10e-50
    return (f(x+h) - f(x)) / h

if __name__=="__main__":
    print("Rounding error example: 1e-50 ->",np.float32(1e-50))

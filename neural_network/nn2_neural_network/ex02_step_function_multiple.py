import numpy as np

def step_function(x):
    y = x > 0
    return y.astype(int)

if __name__=="__main__":
    print(step_function(np.array([1,2,3])))

import numpy as np

def step_function(x):
    if x > 0:
        return 1
    else:
        return 0

if __name__=="__main__":
    print(step_function(3.0))
    # step_function(np.array([1,2,3])) 
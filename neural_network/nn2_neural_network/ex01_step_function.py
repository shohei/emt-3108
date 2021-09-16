import numpy as np
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.abspath(__file__),"../../")))
sys.path.append(os.path.abspath(os.path.join(os.path.abspath(__file__),"../../../")))

def step_function(x):
    if x > 0:
        return 1
    else:
        return 0

if __name__=="__main__":
    print(step_function(3.0))
    # step_function(np.array([1,2,3])) 
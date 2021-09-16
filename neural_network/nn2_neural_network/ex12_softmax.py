import numpy as np
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.abspath(__file__),"../../")))
sys.path.append(os.path.abspath(os.path.join(os.path.abspath(__file__),"../../../")))

def softmax(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

if __name__=="__main__":
    a = np.array([0.3, 2.9, 4.0])
    y = softmax(a)
    print(y) #[ 0.01821127 0.24519181 0.73659691] 
    print(np.sum(y)) # 1.0
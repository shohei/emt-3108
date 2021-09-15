import numpy as np

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c) 
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

if __name__=="__main__":
    a = np.array([0.3, 2.9, 4.0])
    y = softmax(a)
    print(y) #[ 0.01821127 0.24519181 0.73659691] 
    print(np.sum(y)) # 1.0
import numpy as np

def max_Qval(s, Qtable):
    # Add your code below

    return maxQ, max_as 

if __name__=="__main__":
    num_s = 5
    num_a = 10
    Qtable = np.zeros((num_s,num_a))
    
    Qtable[3][2] = 9
    Qtable[3][4] = 6 
    maxQ, max_as = max_Qval(3, Qtable)
    print(f"max Q={maxQ}, actions={max_as}")

# Expected result
# max Q=9.0, actions=[2]
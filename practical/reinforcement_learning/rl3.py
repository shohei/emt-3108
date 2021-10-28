import numpy as np
import random

def select_action(s, Qtable):
    # Add your code

    return maxQ, max_a 

if __name__=="__main__":
    num_a = 5
    num_s = 10
    Qtable = np.zeros((num_s,num_a))
    
    Qtable[3][2] = 9
    Qtable[4][4] = 9 
    Qtable[5][1] = 9 
    
    for s in range(num_s):
        maxQ, a = select_action(s, Qtable)
        print(f"s={s}, a={a}")

# Expected result
# s=0, a=2
# s=1, a=4
# s=2, a=4
# s=3, a=2
# s=4, a=4
# s=5, a=1
# s=6, a=2
# s=7, a=2
# s=8, a=2
# s=9, a=1
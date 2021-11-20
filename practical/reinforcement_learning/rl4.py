import numpy as np

from rl3 import select_action

def epsilon_greedy(epsilon, s, num_a, Qtable):
    # Add your code 

    return a 

if __name__=="__main__":
    num_s = 10
    num_a = 5
    Qtable = np.zeros((num_s,num_a))

    Qtable[3][1] = 9
    # Qtable[4][4] = 9 
    # Qtable[5][1] = 9 

    actions = []
    for i in range(100):
        epsilon = 0.2
        s = 3
        a = epsilon_greedy(epsilon, s, num_a, Qtable)
        print(f"s={s},a={a}")
        actions.append(a)

    print(np.unique(actions, return_counts=True))

# Expected result
# s=3,a=1
# s=3,a=4
# ...
# s=3,a=1
# s=3,a=1
# (array([0, 1, 2, 3, 4]), array([ 4, 80,  5,  7,  4]))
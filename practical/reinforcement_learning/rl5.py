import numpy as np
TRIAL_MAX = 100
num_a = 2
num_s = 2
epsilon = 0.1
alpha = 0.5
gamma = 0.9

from rl1 import cheese_machine 
from rl2 import max_Qval
from rl4 import epsilon_greedy

if __name__=="__main__":
    Qtable = np.zeros((num_s,num_a))
    s = 0
    s2 = 0
    for i in range(TRIAL_MAX):
        a = epsilon_greedy(epsilon, s, num_a, Qtable)
        reward, s2 = cheese_machine(s,a)
        Q_max, _ = max_Qval(s2, Qtable)
        Qtable[s][a] = (1-alpha)*Qtable[s][a] + alpha*(reward+gamma*Q_max)
        s = s2
        # if reward>0:
        #     print(f"success: s={s}, a={a}")
    print(Qtable)

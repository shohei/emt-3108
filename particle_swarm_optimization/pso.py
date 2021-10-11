import numpy as np
import random
import pdb
import matplotlib.pyplot as plt

T = 100

N_bit = 10
N = 20 
x = np.random.rand(N,N_bit)
v = np.random.rand(N,N_bit)
g = np.zeros(N_bit)
p = np.zeros((N,N_bit))
w = 0.8 
c1 = 1
c2 = 1

def evalOneMax(x):
    for xj in x:
        if xj>1:
            return 0
    return sum(x)

gs = []
for gen in range(T):
    for i in range(N):
        for j in range(N_bit):
            vj = w*v[i,j] + random.random()*c1*(p[i,j]-x[i,j])+random.random()*c2*(g[j]-x[i,j])
            xj = x[i,j] + vj
            x[i,j] = xj.copy()
            v[i,j] = vj.copy()
        val_xi = evalOneMax(x[i]) 
        val_pi = evalOneMax(p[i])
        val_g = evalOneMax(g)
        if val_xi > val_pi:
            p[i] = x[i].copy()
        if val_xi > val_g:
            g = x[i].copy()
    print(val_g)
    gs.append(val_g)

plt.plot(gs)
plt.show()
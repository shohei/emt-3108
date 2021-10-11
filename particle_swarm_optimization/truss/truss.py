import numpy as np
import matplotlib.pyplot as plt
import pdb
import random

def meshtruss(p1,p2,nx,ny): 
    nodes = []
    bars = []
    xx = np.linspace(p1[0],p2[0],nx+1) 
    yy = np.linspace(p1[1],p2[1],ny+1) 
    for y in yy:
        for x in xx:
            nodes.append([x,y]) 
    for j in range(ny):
        for i in range(nx): 
            n1 = i + j*(nx+1) 
            n2 = n1 + 1
            n3 = n1 + nx + 1
            n4 = n3 + 1
            bars.extend([[n1,n2],[n1,n3],[n1,n4],[n2,n3]])
        bars.append([n2,n4])
    index = ny*(nx+1) + 1 
    for j in range(nx):
        bars.append([index+j-1,index+j]) 
    return np.array(nodes), np.array(bars)

coord, connec =  meshtruss((0,0),(0.6,0.4),6,4)
print(coord)
print(connec)

# def opttruss(coord,connec,E,F,freenode,V0,plotdisp=False): 
n = connec.shape[0] # number of trusses
m = coord.shape[0] # number of points
vectors = coord[connec[:,1],:] - coord[connec[:,0],:] 
l = np.sqrt((vectors**2).sum(axis=1))
e = vectors.T/l
B = (e[np.newaxis] * e[:,np.newaxis]).T

E0=1e+7
E = E0*np.ones(connec.shape[0])
loads = np.zeros_like(coord)
loads[20,1] = -100.
F = loads
free = np.ones_like(coord).astype('int')
free[::7,:]=0
freenode = free
# V0 = 0.1
V0 = 5 

def volume(x):
    return (x * l).sum(), l

xmin = 1e-6 * np.ones(n) 
xmax = 1e-2 * np.ones(n)
totalvolume = volume(xmax)[0]

def evalTruss(x):
    for xi in x:
        if xi<0:
            return 0,
    current_volume  = volume(x)[0]
    if current_volume > V0:
        return 0,

    D = E * x/l
    kx = e * D
    K = np.zeros((2*m, 2*m))
    for i in range(n):
        aux = 2*connec[i,:]
        index = np.r_[aux[0]:aux[0]+2, aux[1]:aux[1]+2]
        k0 = np.concatenate((np.concatenate((B[i],-B[i]),axis=1), \
                            np.concatenate((-B[i],B[i]),axis=1)), axis=0)
        K[np.ix_(index,index)] = K[np.ix_(index,index)] + D[i] * k0
    block = freenode.flatten().nonzero()[0] 
    matrix = K[np.ix_(block,block)]
    rhs = F.flatten()[block]
    try:
        solution = np.linalg.solve(matrix,rhs) 
    except Exception:
        return 0,
    u = freenode.astype('float').flatten() 
    u[block] = solution
    U = u.reshape(m,2)
    axial = ((U[connec[:,1],:] - U[connec[:,0],:]) * kx.T).sum(axis =1)
    stress = axial / x
    cost = (U * F).sum()
    obj = 1/cost
    # dcost = -stress**2 / E * l 
    # return cost, dcost, U, stress
    return obj,stress,U

T = 100 
N = 20 
x = 1e-6*np.ones((N,n))
# x = np.random.rand(N,n)
v = np.random.rand(N,n)
# g = 1e-4*np.ones(n)
# p = 1e-4*np.ones((N,n))
g = np.zeros(n)
p = np.zeros((N,n))
w = 0.8 
c1 = 1
c2 = 1 

gs = []
for gen in range(T):
    for i in range(N):
        for j in range(n):
            vj = w*v[i,j] + random.random()*c1*(p[i,j]-x[i,j])+random.random()*c2*(g[j]-x[i,j])
            xj = x[i,j] + vj
            x[i,j] = xj.copy()
            v[i,j] = vj.copy()
        val_xi = evalTruss(x[i])[0]
        val_pi = evalTruss(p[i])[0]
        val_g = evalTruss(g)[0]
        if val_xi > val_pi:
            p[i] = x[i].copy()
        if val_xi > val_g:
            g = x[i].copy()
    print(val_g,g)
    gs.append(val_g)
plt.plot(gs)

# plotdisp = True
plotdisp = False 
def drawTruss(x,factor=3, wdt=5e2): 
    _,stress,U = evalTruss(x)
    newcoor = coord + factor*U
    if plotdisp:
        fig = plt.figure(figsize=(12,6)) 
        ax = fig.add_subplot(121)
        bx = fig.add_subplot(122)
    else:
        fig = plt.figure()
        ax = fig.add_subplot(111) 
    for i in range(n):
        bar1 = np.concatenate( (coord[connec[i,0],:][np.newaxis],
        coord[connec[i,1],:][np.newaxis]),axis=0 )
        bar2 = np.concatenate( (newcoor[connec[i,0],:][np.newaxis],newcoor[connec[i,1],:][np.newaxis]),axis=0) 
    if stress[i] > 0:
        clr = 'r'
    else:
        clr = 'b'
    ax.plot(bar1[:,0],bar1[:,1], color = clr, linewidth = wdt * x [i])
    ax.axis('equal')
    ax.set_title('Stress') 
    if plotdisp:
        bx.plot(bar1[:,0],bar1[:,1], 'r:') 
        bx.plot(bar2[:,0],bar2[:,1], color = 'k', linewidth= wdt* x[i]) 
        bx.axis('equal')

drawTruss(g)

plt.show()
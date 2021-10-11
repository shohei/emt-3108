import numpy as np
import matplotlib.pyplot as plt
import pdb

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
V0 = 0.1

def fobj(x):
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
    solution = np.linalg.solve(matrix,rhs) 
    u = freenode.astype('float').flatten() 
    u[block] = solution
    U = u.reshape(m,2)
    axial = ((U[connec[:,1],:] - U[connec[:,0],:]) * kx.T).sum(axis =1)
    stress = axial / x
    cost = (U * F).sum()
    dcost = -stress**2 / E * l 
    return cost, dcost, U, stress

def volume(x):
    return (x * l).sum(), l

xmin = 1e-6 * np.ones(n) 
xmax = 1e-2 * np.ones(n)
f = lambda x: fobj(x)[0]
derf = lambda x: fobj(x)[1]
totalvolume = volume(xmax)[0]
constr = lambda x: 1./totalvolume * volume(x)[0] - V0 
dconstr= lambda x: 1./totalvolume * volume(x)[1]
x0 = 1e-4*np.ones(n)

pdb.set_trace()
# problem = NLP(f,x0,df=derf,c=constr,dc=dconstr, lb=xmin, ub=xmax, name='Truss', iprint=100)
# result = problem.solve("mma")




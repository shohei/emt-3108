from deap import creator, base, tools, algorithms
import random
import struct
from control.matlab import *
import numpy as np
import pdb
import sys
np.seterr(over='ignore')

def bin_to_float32(binary_string):
    f = int(binary_string, 2)
    float32 = struct.unpack('f', struct.pack('I', f))[0]
    return float32

creator.create("fitness", base.Fitness, weights=(-1.0,))
creator.create("individual",list,fitness=creator.fitness)

toolbox = base.Toolbox()
toolbox.register('attr_bool',random.randint,0,1)
toolbox.register('individual',tools.initRepeat,creator.individual, toolbox.attr_bool,n=32*3)
toolbox.register('population',tools.initRepeat,list,toolbox.individual)

Q = 1 
R = 0.01
dt = 0.1
t = np.arange(0,20,dt)
s = tf('s')
G = 3/(s**2+s+1)
FLT_MAX = sys.float_info.max
def evalLQ(individual):
    Kp_binary = individual[:32]
    Ki_binary = individual[32:64]
    Kd_binary = individual[64:]
    Kp_binary_string = ''.join([str(k) for k in Kp_binary])
    Ki_binary_string = ''.join([str(k) for k in Ki_binary])
    Kd_binary_string = ''.join([str(k) for k in Kd_binary])
    Kp_float32 = bin_to_float32(Kp_binary_string) 
    Ki_float32 = bin_to_float32(Ki_binary_string) 
    Kd_float32 = bin_to_float32(Kd_binary_string) 
    K = Kp_float32 + Ki_float32/s + Kd_float32*s/(1+0.1*s)
    loop = series(K,G)
    closedLoop = feedback(loop, 1)
    try:
        y,_ = step(closedLoop,t)
    except Exception:
        J = FLT_MAX
        return J,
    u,_,_ = lsim(K, 1-y, t)
    J = dt*sum(Q*(1-y)**2 + R*u**2)
    if np.isnan(J):
        J = FLT_MAX
    return J,

toolbox.register('evaluate',evalLQ)
toolbox.register('mate',tools.cxTwoPoint)
toolbox.register('mutate',tools.mutFlipBit,indpb=0.05)
toolbox.register('select',tools.selTournament,tournsize=20)

def printResult(individual):
    bestFit = individual.fitness.values[0]
    Kp_binary = individual[:32]
    Ki_binary = individual[32:64]
    Kd_binary = individual[64:]
    Kp_binary_string = ''.join([str(k) for k in Kp_binary])
    Ki_binary_string = ''.join([str(k) for k in Ki_binary])
    Kd_binary_string = ''.join([str(k) for k in Kd_binary])
    Kp_float32 = bin_to_float32(Kp_binary_string) 
    Ki_float32 = bin_to_float32(Ki_binary_string) 
    Kd_float32 = bin_to_float32(Kd_binary_string) 
    print("Kp:{}, Ki:{}, Kd:{}, J:{}".format(Kp_float32,Ki_float32,Kd_float32,bestFit))

population = toolbox.population(n=100)
GEN = 300
CXPB = 0.8
MUTPB = 0.1
for gen in range(GEN):
    offspring = algorithms.varAnd(population, toolbox, cxpb=CXPB, mutpb=MUTPB)
    fits = toolbox.map(toolbox.evaluate, offspring)
    for fit, ind in zip(fits, offspring):
        ind.fitness.values = fit
    population = toolbox.select(offspring, k=len(population))
    best = tools.selBest(population, 1)[0]
    bestFit = best.fitness.values[0]
    # print(gen, bestFit)
    print(gen,end=' ')
    printResult(best)

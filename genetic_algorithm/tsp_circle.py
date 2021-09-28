from deap import base, creator, tools
import numpy as np
import random
import math
import matplotlib.pyplot as plt 

from scipy.spatial import distance

# ANIMATE = False
ANIMATE = True 

if ANIMATE:
    NUM_CITIES  = 20 
    NGEN = 200
else:
    NUM_CITIES  = 6 
    NGEN = 100

RANGE = 1000

def generate_cities( n ):
    return list((RANGE/2*math.cos(i*math.pi*2/n)+RANGE/2,RANGE/2*math.sin(i*math.pi*2/n)+RANGE/2)for i in range( n))

creator.create("Fitness", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.Fitness)

toolbox = base.Toolbox()
toolbox.register("attribute", np.random.permutation, NUM_CITIES)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.attribute)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evalSalesman( individual ):
    td = 0
    for k in range(len(individual)+1):
        i = individual[k-2]
        j = individual[k-1]
        d = distance.euclidean(list(cities)[i],list(cities)[j])
        td +=d
    return ( td, )

toolbox.register("evaluate", evalSalesman)
toolbox.register( "mate", tools.cxOrdered )
toolbox.register( "mutate", tools.mutShuffleIndexes, indpb=0.05 )
toolbox.register("select", tools.selTournament, tournsize=3)

def generate_px_py_pn(ind):
    d = 0
    px, py, pn = [], [], []
    for i in range(NUM_CITIES+1):
        n1 = ind[i-2]
        n2 = ind[i-1]
        d += distance.euclidean(list(cities)[n1], list(cities)[n2])
        # print("%s, %s, %s" % (n1, list(cities)[n1][0], list(cities)[n1][1]))
        px += [list(cities)[n1][0]]
        py += [list(cities)[n1][1]]
        pn += [n1]
        plt.annotate(n1, xy=(list(cities)[n1][0], list(cities)[n1][1]),fontsize=18)
        plt.annotate('', xy=(list(cities)[n1][0], list(cities)[n1][1]),xytext=(list(cities)[n2][0], list(cities)[n2][1]),
                     arrowprops=dict(arrowstyle='-|>', connectionstyle='arc3',facecolor='gray', edgecolor='gray'))
    return px, py, pn

def plot_route(gen,ind):
    plt.subplots(figsize=(6, 6))
    plt.xlim(0, RANGE)
    plt.ylim(0, RANGE)
    plt.grid(True)
    plt.text(0, 0, 'iter={}'.format(gen), fontsize=12)
    lines, = plt.plot(0, 0, marker='o', color='k', markersize=3, linestyle='None')
    px, py, pn = generate_px_py_pn(ind)
    lines.set_data(px, py)
    plt.pause(0.01)

def varAnd(population, toolbox, cxpb, mutpb):
    offspring = [toolbox.clone(ind) for ind in population]
    for i in range(1, len(offspring), 2):
        if random.random() < cxpb:
            offspring[i - 1], offspring[i] = toolbox.mate(offspring[i - 1],
                                                          offspring[i])
            del offspring[i - 1].fitness.values, offspring[i].fitness.values
    for i in range(len(offspring)):
        if random.random() < mutpb:
            offspring[i], = toolbox.mutate(offspring[i])
            del offspring[i].fitness.values
    return offspring

def eaSimple(population, toolbox, cxpb, mutpb, ngen):
    invalid_ind = [ind for ind in population if not ind.fitness.valid]
    fitnesses = toolbox.map(toolbox.evaluate, invalid_ind)
    for ind, fit in zip(invalid_ind, fitnesses):
        ind.fitness.values = fit
    for gen in range(1, ngen + 1):
        offspring = toolbox.select(population, len(population))
        offspring = varAnd(offspring, toolbox, cxpb, mutpb)
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = toolbox.map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit
        population[:] = offspring
        bestInd = tools.selBest(population, 1)[0]
        bestFit = bestInd.fitness.values
        print(gen, bestFit, bestInd)
        if ANIMATE:
            plot_route(gen, bestInd)

random.seed(1)
cities = generate_cities( NUM_CITIES )
pop = toolbox.population(n=100)
eaSimple(pop, toolbox, cxpb = 0.8, mutpb=0.2, ngen=NGEN)
best_ind = tools.selBest(pop, 1)[0]
print("Best individual is %s" % (best_ind))
print(evalSalesman(best_ind))

if not ANIMATE:
    px, py, pn = generate_px_py_pn(best_ind)
    plt.xlim(0, RANGE)
    plt.ylim(0, RANGE)
    plt.grid(True)
    plt.plot(px, py, marker="o", color='k', markersize=3,linestyle='None')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

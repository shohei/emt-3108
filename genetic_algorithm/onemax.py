from deap import creator, base, tools, algorithms
import random

creator.create("fitness", base.Fitness, weights=(1.0,))
creator.create("individual",list,fitness=creator.fitness)

toolbox = base.Toolbox()
toolbox.register('attr_bool',random.randint,0,1)
toolbox.register('individual',tools.initRepeat,creator.individual, toolbox.attr_bool,n=100)
toolbox.register('population',tools.initRepeat,list,toolbox.individual)

def evalOneMax(individual):
    return sum(individual),

toolbox.register('evaluate',evalOneMax)
toolbox.register('mate',tools.cxTwoPoint)
toolbox.register('mutate',tools.mutFlipBit,indpb=0.05)
toolbox.register('select',tools.selTournament,tournsize=3)

population = toolbox.population(n=100)
GEN = 1000
CXPB = 0.5
MUTPB = 0.2
for gen in range(GEN):
    offspring = algorithms.varAnd(population, toolbox, cxpb=CXPB, mutpb=MUTPB)
    fits = toolbox.map(toolbox.evaluate, offspring)
    for fit, ind in zip(fits, offspring):
        ind.fitness.values = fit
    population = toolbox.select(offspring, k=len(population))
    best = tools.selBest(population, 1)[0]
    bestFit = best.fitness.values[0]
    print(gen, bestFit)
    if bestFit==100:
        break

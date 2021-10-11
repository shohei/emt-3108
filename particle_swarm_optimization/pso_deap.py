import operator
import random
from deap import base
from deap import creator
from deap import tools
import matplotlib.pyplot as plt
import pdb

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Particle", list, fitness=creator.FitnessMax, speed=list, 
    smin=None, smax=None, best=None)

def generate(size, pmin, pmax, smin, smax):
    part = creator.Particle(random.uniform(pmin, pmax) for _ in range(size)) 
    part.speed = [random.uniform(smin, smax) for _ in range(size)]
    return part

def updateParticle(part, best, phi1, phi2):
    u1 = (random.uniform(0, phi1) for _ in range(len(part)))
    u2 = (random.uniform(0, phi2) for _ in range(len(part)))
    v_u1 = map(operator.mul, u1, map(operator.sub, part.best, part))
    v_u2 = map(operator.mul, u2, map(operator.sub, best, part))
    w = 0.8
    part.speed = list(map(lambda x: w*x, part.speed))
    part.speed = list(map(operator.add, part.speed, map(operator.add, v_u1, v_u2)))
    part[:] = list(map(operator.add, part, part.speed))

def evalOneMax(ind):
    for xi in ind:
        if xi>1:
            return 0,
    return sum(ind),

toolbox = base.Toolbox()
toolbox.register("particle", generate, size=10, pmin=-1, pmax=1, smin=-1, smax=1)
toolbox.register("population", tools.initRepeat, list, toolbox.particle)
toolbox.register("update", updateParticle, phi1=1.0, phi2=1.0)
toolbox.register("evaluate", evalOneMax)

fits= []
def main():
    pop = toolbox.population(n=20)
    GEN = 100
    best = None

    for g in range(GEN):
        for part in pop:
            part.fitness.values = toolbox.evaluate(part)
            if not part.best or part.best.fitness < part.fitness:
                part.best = creator.Particle(part)
                part.best.fitness.values = part.fitness.values
            if not best or best.fitness < part.fitness:
                best = creator.Particle(part)
                best.fitness.values = part.fitness.values
        for part in pop:
            toolbox.update(part, best)

        print(best,best.fitness.values) 
        fits.append(best.fitness.values)
    return pop, best

if __name__ == "__main__":
    main()
    plt.plot(fits)
    plt.show()

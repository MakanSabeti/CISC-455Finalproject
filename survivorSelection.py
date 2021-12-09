'''
Name: Makan Sabeti
Student number: 20118161
Description: This will be done by generational replacement. This will take the parents with the worst fitness and
replace them with the offspring pool.
'''

def generationalReplacement(currentPop, currentFitness, offspring, offspringFitness):

    population = []
    fitness = []

    x = len(offspring)
    # sort the parents by fitness
    current_fitness, current_pop = zip(*sorted(zip(currentFitness, currentPop)))
    current_pop = list(current_pop)
    current_fitness = list(current_fitness)
    # replace the worst ranked with all of the offspring
    population[0:x] = offspring
    population[x:] = current_pop[x:]
    fitness[0:x] = offspringFitness
    fitness[x:] = current_fitness[x:]

    return population, fitness

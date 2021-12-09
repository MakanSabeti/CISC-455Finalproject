'''
Name: Makan Sabeti
Student number: 201118161
Description: This will be a GP mutation change. There will be a single point that will get changed.
'''
import random

def permutationSwap(individual):
    """Mutate a draft selection"""

    mutant = individual.copy()

    # picking two random indices from 0 to individual
    mutant1 = random.randint(0, len(individual) - 1)
    mutant2 = random.randint(0, len(individual) - 1)
    # storing the value at the index
    a = mutant[mutant1]
    b = mutant[mutant2]
    # changing values
    mutant[mutant1] = b
    mutant[mutant2] = a

    return mutant
'''
Name: Makan Sabeti
Student Number: 20118161
Description: For this function we will perform cut-and-crossfill crossover
'''

import random


def crossover(parent1, parent2):
    """cut-and-crossfill crossover for permutation representations"""

    offspring1 = []
    offspring2 = []

    # We need to take the the start to random index point of both parent 1 and parent 2 and add them to offspring 1
    # and offspring 2 respectively and then combine them with the back of parent 2 and parent 1 respectively.
    max = len(parent1) - 1
    splitIndex = random.randint(0, max)
    offspring1Front = parent1[0:splitIndex]
    offspring2Front = parent2[0:splitIndex]
    offspring1Back = parent2[splitIndex:]
    offspring2Back = parent1[splitIndex:]

    offspring1 = offspring1Front + offspring1Back
    offspring1 = list(offspring1)
    offspring2 = offspring2Front + offspring2Back
    offspring2 = list(offspring2)

    return offspring1, offspring2

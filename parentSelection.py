'''
Name: Makan Sabeti
Student number: 20118161
Description: The parent selection method that I will use is going to be tournament without replacement. Now typically
parent selection for genetic programs are done by fitness proportional selection, however I believe that tournament
selection is going to be more useful to us.
'''

import random


def tournament(fitness, matingPoolSize, tournamentSize):
    """Tournament selection without replacement"""

    selected_to_mate = []

    current_max = 0
    index = 0
    # running the tournament to find the highest possible fitness between 4
    # randomly selected indexes for ever pool size
    for i in range(matingPoolSize):
        for j in range(tournamentSize):
            x = random.randint(0, len(fitness) - 1)
            score = fitness[x]
            if score > current_max:  # checking maximum score
                current_max = score
                index = x
        selected_to_mate.append(index)  # adding the winner of the tournament to the selected_to_mate
        current_max = 0

    return selected_to_mate

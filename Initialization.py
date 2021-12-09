'''
Name: Makan Sabeti
Student number: 20118161
Description: Since I cannot read in the data of the current pool of players for the draft (as they are in different
leagues and you need a paid subscription to see their stats), I have decided to generate my own data. The representation
will be a list of list of list for the population (similar to assignment 2). Each list of list will be a draft pool in
order of first overall to 31st overall. Then inside the list we will have the first index be the player number, then
position then points they got.
'''
import random

def initialization():
    pop = []
    position = ['F', 'D']
    for i in range(20):
        pool = []
        pop.append(pool)
        for j in range(1, 32):
            ind = []
            ind.append(j)
            index = random.randint(0, 1)
            ind.append(position[index])
            points_forward = random.randint(30, 100) #Forwards getting drafted typically put up between 30-100 points
            # Defenders usually put up between 28 and 55 points, therefore we will give them a additional 25 points,
            # this means that they are more unlikely to go first overall, which is typically true. It is rare for a
            # defender to be first, they typically go a little later.
            points_defenders = random.randint(28, 55)
            points_defenders += 25
            if position[index] == 'F':
                ind.append(points_forward)
            else:
                ind.append(points_defenders)
            pool.append(ind)
    return pop

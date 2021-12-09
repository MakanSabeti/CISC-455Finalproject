'''
Name: Makan Sabeti
Student number: 20118161
Description: The fitness actually took me a while to come up with. I decided to go with having previous data from years
before and use that as training. I will be doing a error comparison. Every time a person drafted after has a more points
than the guy before then that's a error.
'''
import random

def newPlayers(pool):
    error = 0
    for i in range(len(pool) - 1):
        current = pool[i]
        compared = pool[i+1]
        if current[2] < compared[2]:
            error += 1
        elif current[2] == compared[2]:
            # If the two players have the same number of points the defender will be drafted in front of the
            # forward because it is more rare for the defender to put up good numbers
            if compared[1] == 'D' and current[1] != 'D':
                error +=1
    error = 31-error
    return error

def oldPlayers(pool):
    oldError = []
    for draft in pool:
        error = 0
        for i in range (len(draft) - 1):
            current = draft[i]
            compared = draft[i+1]
            if current[1] == 'D':
                if i != 1:
                    current[2] += 25
                    #print(current)
            if compared[1] == 'D':
                if i == 0:
                    compared[2] += 25
                    #print(compared)
                elif i == len(draft) - 1:
                    compared[2] += 25
                    #print(compared)
            if current[2] < compared[2]:
                error += 1
            elif current[2] == compared[2]:
                # If the two players have the same number of points the defender will be drafted in front of the
                # forward because it is more rare for the defender to put up good numbers
                if compared[1] == 'D' and current[1] != 'D':
                    error +=1
        error = 31 - error
        oldError.append(error)
    return oldError

def error(newDraft, oldDraft):
    temp = []
    fitness = 0
    for i in range(len(oldDraft)):
        value = newDraft - oldDraft[i]
        value = value * value
        temp.append(value)
    for j in range(len(temp)):
        fitness = fitness + temp[j]
    return fitness

def fitness(newP, oldP):
    newDraft = newPlayers(newP)
    oldDraft = oldPlayers(oldP)
    fitness = error(newDraft, oldDraft)
    return fitness
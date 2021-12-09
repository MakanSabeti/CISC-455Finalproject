'''
Name: Makan Sabeti
Student number: 20118161
'''
import random
from lib2to3.pgen2 import driver
import numpy
import pandas as pd
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

import Initialization
import Fitness
import Recombination
import Mutation
import parentSelection
import survivorSelection

def main():
    #First thing we need to do is webscrape the hockey data. The data is going to be the number they got drafted, their
    #position and the amount of points they put up since they got drafted.
    url = 'https://www.hockeydb.com/ihdb/draft/nhl2017e.html'
    years = [2015, 2016, 2017, 2018, 2019]
    allPool = []
    for year in years:
      url = f'https://www.hockeydb.com/ihdb/draft/nhl{year}e.html'
      response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
      soup = BeautifulSoup(response.text, "html.parser")
      pool = []
      #Before 2016 there were only 30 teams in the NHL, therefore we need to account for that
      if year >2016:
        for tr in soup.find_all('tr')[2:33]:
            tds = tr.find_all('td')
            if tds[9].text != '':
                pool.append([tds[1].text, tds[4].text, int(tds[9].text)])
            else:
                pool.append([tds[1].text, tds[4].text, 12])
      else:
        for tr in soup.find_all('tr')[2:31]:
            tds = tr.find_all('td')
            if tds[9].text != '':
                pool.append([tds[1].text, tds[4].text, int(tds[9].text)])
            else:
                pool.append([tds[1].text, tds[4].text, 12])


      allPool.append(pool)
    #allPool will be a list of list of list with each draft in the list of list and each list is the players


    '''Now that we have imported all the data that we need we can begin the genetic algorithm'''

    random.seed()
    numpy.random.seed()
    popsize = 20
    mating_pool_size = int(popsize * 0.5)  # has to be even
    tournament_size = 4
    xover_rate = 0.9
    mut_rate = 0.2
    gen_limit = 31

    # initialize population
    gen = 0  # initialize the generation counter
    population = Initialization.initialization()
    fitness = []
    for draft in range(len(population)):
        print(draft)
        fitness.append(Fitness.fitness(population[draft], allPool))
    print("generation", gen, ": best fitness", max(fitness), "taverage fitness", sum(fitness) / len(fitness))

    # evolution begins
    while gen < gen_limit:

        # pick parents
        print(fitness)
        parents_index = parentSelection.tournament(fitness, mating_pool_size, tournament_size)

        # in order to randomly pair up parents
        random.shuffle(parents_index)

        # reproduction
        offspring = []
        offspring_fitness = []
        i = 0  # initialize the counter for parents in the mating pool

        # offspring are generated using selected parents in the mating pool
        while len(offspring) < mating_pool_size:

            # recombination
            if random.random() < xover_rate:
                off1, off2 = Recombination.crossover(population[parents_index[i]],
                                                                         population[parents_index[i + 1]])
            else:
                off1 = population[parents_index[i]].copy()
                off2 = population[parents_index[i + 1]].copy()

            # mutation
            if random.random() < mut_rate:
                off1 = Mutation.permutationSwap(off1)
            if random.random() < mut_rate:
                off2 = Mutation.permutationSwap(off2)

            offspring.append(off1)
            offspring_fitness.append(Fitness.fitness(off1, allPool))
            offspring.append(off2)
            offspring_fitness.append(Fitness.fitness(off2, allPool))
            i = i + 2  # update the counter

        # organize the population of next generation
        population, fitness = survivorSelection.generationalReplacement(population, fitness, offspring, offspring_fitness)

        gen = gen + 1  # update the generation counter
        print("generation", gen, ": best fitness", max(fitness), "average fitness", sum(fitness) / len(fitness))

    # evolution ends

    # print the final best solution(s)
    bestSolution = []
    bestFitness = 0
    k = 0
    for i in range(0, popsize):
        if fitness[i] == max(fitness):
            print("best solution", i, population[i], fitness[i])


# end of main
main()
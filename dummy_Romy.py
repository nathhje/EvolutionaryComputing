################################
# EvoMan FrameWork - V1.0 2016 #
# Author: Karine Miras         #
# karine.smiras@gmail.com      #
################################

# imports framework
import sys, os
sys.path.insert(0, 'evoman')
from environment import Environment
from ai_controller import player_controller
from operator import itemgetter
from functions_romy import *
import random
import matplotlib.pyplot as plt
from mutation import mutate

# Gene: controllers
# Individual: single list of controllers
# Population: collection of controllers/individuals

# 1. Create the population
# 2. Determine fitness
# 3. Select the mating pool
# 4. Breed
# 5. Mutate
# 6. Repeat


### START ###
experiment_name = 'dummy_demo'
if not os.path.exists(experiment_name):
    os.makedirs(experiment_name)

# def nextgeneration(current_generation, mutation_rate):
    # pop_ranked = rank_scores(current_generation) #2

# The genetic algorithm
def main(pop_size, mutation_rate, nr_generations):
    growth = []

    # 1. Create the population
    population = initial_population(pop_size)

    for j in range(nr_generations):
        # population = nextgeneration(population, mutation_rate)
        listscores = []
        genfitness = 0

        # 2. Determine fitness
        # check for the entire population the fitness
        for index, data in enumerate(population):
            fitness = fitnesscheck(data)
            listscores.append([index, fitness])
            genfitness += fitness

        print("De "+ str(j) + "e generatie heeft een gemiddelde score van ", genfitness/pop_size)


        # Make N new individuals for the next generation
        newpopulation = []
        for i in range(pop_size):
            # 3. Select the mating pool
            # Kiest twee parents tournament style
            win1, win2 = pickparents(pop_size, listscores)

            # 4. Breed
            # Crossbreed een nieuw child
            newpopulation.append(cross(population[win1], population[win2]))

            # 5. Mutate
            mutation_decision = random.randint(0, 100)

            if mutation_decision > 90:
                mutate(newpopulation[i])

        population = newpopulation
        growth.append(genfitness/pop_size)

    print(growth)
    plt.plot(growth)
    plt.show()

    with open("endresult.txt", "w") as txt_file:
        for data in population:
            for line in data:
                txt_file.write(" ".join(str(line)) + "\n")



######
# Run the genetic algorithm
if __name__ == '__main__':
    main(pop_size=20, mutation_rate=0.01, nr_generations=30)

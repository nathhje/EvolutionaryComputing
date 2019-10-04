###################################
# EvoMan FrameWork - 2020         #
# Authors: Julia Anten,           #
# Jasper den Duijf, Romy Meester, #
# Nathalie van Sterkenburg        #
###################################

# 1. Create the population
# 2. Determine fitness
# 3. Select the mating pool
# 4. Breed
# 5. Mutate
# 6. Repeat

# imports framework
import sys, os
sys.path.insert(0, 'evoman')
from environment import Environment
from ai_controller import player_controller
from operator import itemgetter
from smart_functions import *
import random
import matplotlib.pyplot as plt


### START ###
experiment_name = 'dummy_demo'
if not os.path.exists(experiment_name):
    os.makedirs(experiment_name)

# The genetic algorithm
def main(pop_size, mutation_rate, nr_generations, parentchoice="Tournament", enemy = 1):
    growth = []
    generation = 0

    # 1. Create the population
    population = initial_population(pop_size)

    # Stop calculating when the last 3 generations have the same fitness
    while generation < nr_generations:
        if generation > 3 and sum(np.diff((growth[generation - 3], growth[generation - 2], growth[generation-1]))) == 0:
            break

        listscores = []
        genfitness = 0

        # 2. Determine fitness
        # check for the entire population the fitness
        for index, data in enumerate(population):
            fitness = fitnesscheck(data, enemy = [enemy])

            # save best results individuals bigger than a fitness of 90
            if fitness > 90:
                save_good_result(data,fitness,generation,parentchoice,mutation_rate,enemy)
            listscores.append([index, fitness])
            genfitness += fitness

        print("The "+ str(generation) + "th generation has a mean score of ", genfitness/pop_size)

        # Make N new individuals for the next generation
        newpopulation = []
        if parentchoice != "Tournament":
            listscores = cumsort(listscores)

        for i in range(int(pop_size/2)):
            # 3. Select the mating pool
            # Pick two parents for either the tournament or fitness proportionate style
            if parentchoice == "Tournament":
                win1, win2 = pickparents(pop_size, listscores)
            else:
                win1, win2 = pickparentscumsort(listscores)

            # 4. Breed
            # Crossbreed a new child
            child1,child2 = cross(population[win1], population[win2])
            newpopulation.append(child1)
            newpopulation.append(child2)

            # 5. Mutate
            mutate(newpopulation[i], mutation_rate)

        population = newpopulation
        growth.append(genfitness/pop_size)

        generation = generation + 1

    return growth

def save_data(growth,parentchoice,mutation_rate,enemy):

    with open("growthresults/growthresults"+ parentchoice+ "level"+ str(enemy) +"mutation"+ str(mutation_rate) +".txt", "w") as txt_file:

        for row in growth:
            txt_file.write(str(row)+"\n")


def save_good_result(data,fitness,generation,parentchoice,mutation_rate,enemy):

    with open("bestresults/bestresultgeneration" + str(generation) + "fitness"+ str(fitness) + parentchoice+ "level"+ str(enemy) +"mutation"+ str(mutation_rate) +".txt", "w") as txt_file:
        for line in data:
            txt_file.write(" ".join(str(line)) + "\n")

#####
# Run the genetic algorithm
if __name__ == '__main__':

    selection = "Fitness" # Tournament or fitness proportionate (Density)
    m_rate = 0.01 # 0.005, 0.01, 0.015, 0.02, 0.025, 0.03
    level = 6 # 1, 6, 8

    with open("teststructure.txt", "a") as txt_file:
        txt_file.write("And again \n")

    hist = []
    thegrowths = []
    for i in range(20):
        thegrowths.append(main(pop_size=40, mutation_rate=m_rate, nr_generations=60, parentchoice=selection, enemy = level))
        with open("teststructure.txt", "a") as txt_file:
            txt_file.write(str(thegrowths[-1])+ "\n")
        hist.append(thegrowths[-1][-1])

    # Save the data of the fitness over the generations
    save_data(thegrowths,selection,m_rate,level)

    # Plot the outcomes of the last generations
    plt.hist(hist)
    plt.show()

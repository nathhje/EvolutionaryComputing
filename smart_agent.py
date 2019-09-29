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
from smart_functions import *
import random
import matplotlib.pyplot as plt

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
def main(pop_size, mutation_rate, nr_generations, parentchoice="Tournament", enemy = 1, runcount = ""):
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
            fitness = fitnesscheck(data, enemy = [enemy])
            listscores.append([index, fitness])
            genfitness += fitness

        print("De "+ str(j) + "e generatie heeft een gemiddelde score van ", genfitness/pop_size)


        # Make N new individuals for the next generation
        newpopulation = []
        if parentchoice != "Tournament":
            listscores = cumsort(listscores)

        for i in range(int(pop_size/2)):
            # 3. Select the mating pool
            # Kiest twee parents tournament style
            if parentchoice == "Tournament":
                win1, win2 = pickparents(pop_size, listscores)
            else:
                win1, win2 = pickparentscumsort(listscores)

            # 4. Breed
            # Crossbreed een nieuw child
            child1,child2 = cross(population[win1], population[win2])
            newpopulation.append(child1)
            newpopulation.append(child2)
            #print("nieuwe ronde, nieuwe kansen")
            #print(win1, win2)

            # 5. Mutate
            mutate(newpopulation[i], mutation_rate)

        population = newpopulation
        growth.append(genfitness/pop_size)

    # Save data
    print(growth)
    save_data(growth, population, runcount, parentchoice, mutation_rate)
    return growth[-1]

def save_data(growth, population, runcount, parentchoice, mutation_rate):
    # Last result of population
    with open("endresult.txt", "w") as txt_file:
        for data in population:
            for line in data:
                txt_file.write(" ".join(str(line)) + "\n")

    # growth results over generations
    with open("growthresults/growthresults" + parentchoice + str(mutation_rate) + "_" + str(runcount) + ".txt", "w") as txt_file:
            txt_file.write(str(growth))
    print("growthresults/growthresults" + parentchoice + str(mutation_rate) + "_" + str(runcount) + ".txt")

def show_results():
    # last result of population
    with open("endresult.txt", "r") as txt_file:
        last_population = txt_file.read()

    # print(last_population)

    # growth results over generations
    with open("growthresults/growthresults" + parentchoice + str(mutation_rate) + "_" + str(runcount) + ".txt", "r") as txt_file:
        growth = txt_file.read().strip("[").strip("]").split(", ")

    growth = [float(x) for x in growth]
    plt.plot(growth)
    plt.show()



#####
# Run the genetic algorithm
if __name__ == '__main__':

    hist = []
    for i in range(1):
        hist.append(main(pop_size=32, mutation_rate=0.02, nr_generations=30, parentchoice="density", runcount = i))

    plt.hist(hist)
    plt.show()

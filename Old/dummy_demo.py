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
from crossbreed import *
import random
import matplotlib.pyplot as plt
from mutation import mutate

experiment_name = 'dummy_demo'
if not os.path.exists(experiment_name):
    os.makedirs(experiment_name)


def main(popsize,gens):
    growth = []

    # Opent random start population
    alldata = genrandomstart(popsize)

    for j in range(gens):
        listscores = []
        genfitness = 0

        # check for the entire population the fitness
        for index, data in enumerate(alldata):
            fitness = fitnesscheck(data)
            listscores.append([index, fitness])
            genfitness += fitness

        print("De "+ str(j) + "e generatie heeft een gemiddelde score van ", genfitness/popsize)

        # Make N new individuals for the next generation
        newpopulation = []
        for i in range(int(popsize/2)):
            # Kiest twee parents tournament style
            win1, win2 = pickparents(popsize, listscores)
            # Crossbreed een nieuw child
            child1,child2 = cross(alldata[win1], alldata[win2])
            newpopulation.append(child1)
            newpopulation.append(child2)
            print("nieuwe ronde, nieuwe kansen")
            for j in range(2):
                print(j)
                mutation_decision = random.randint(0, 100)

                if mutation_decision > 90:
                    mutate(newpopulation[2*i+j])

        alldata = newpopulation
        growth.append(genfitness/popsize)

    print(growth)
    plt.plot(growth)
    plt.show()

    with open("endresult.txt", "w") as txt_file:
        for data in alldata:
            for line in data:
                txt_file.write(" ".join(str(line)) + "\n")

if __name__ == '__main__':
    main(6,30)

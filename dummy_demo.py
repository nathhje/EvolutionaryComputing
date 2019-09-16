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

experiment_name = 'dummy_demo'
if not os.path.exists(experiment_name):
    os.makedirs(experiment_name)

N = 20 #Population size



numbergen = 30
growth = []

# Opent random start population
alldata = genrandomstart(N)

for j in range(numbergen):
    listscores = []
    genfitness = 0

    # check for the entire population the fitness
    for index, data in enumerate(alldata):
        fitness = fitnesscheck(data)
        listscores.append([index, fitness])
        genfitness += fitness

    print("De "+ str(j) + "e generatie heeft een gemiddelde score van ", genfitness/N)

    # Make N new individuals for the next generation
    newpopulation = []
    for i in range(N):
        # Kiest twee parents tournament style
        win1, win2 = pickparents(N, listscores)
        # Crossbreed een nieuw child
        newpopulation.append(cross(alldata[win1], alldata[win2]))

    alldata = newpopulation
    growth.append(genfitness/N)

print(growth)
plt.plot(growth)
plt.show()

with open("endresult.txt", "w") as txt_file:
    for data in alldata:
        for line in data:
            txt_file.write(" ".join(str(line)) + "\n")

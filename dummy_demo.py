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
from crossbreed import cross, pickparents
import random

experiment_name = 'dummy_demo'
if not os.path.exists(experiment_name):
    os.makedirs(experiment_name)

N = 10 #Population size

listscores = []
genfitness = 0

# Opent random start population
for i in range(N):
    with open("randomstart/output"+ str(i) + ".txt") as f:
        lines = f.readlines()
        with open("output.txt", "w") as f1:
            f1.writelines(lines)


    # initializes environment with ai player using random controller, playing against static enemy
    env = Environment(experiment_name=experiment_name, player_controller=player_controller(), speed="fastest")
    env.play()

    # checkt de fitness en slaat het op
    listscores.append([i, env.fitness_single()])
    genfitness += env.fitness_single()

print(genfitness/N)


for i in range(N):
    # Kiest twee parents tournament style
    win1, win2 = pickparents(N, listscores)
    # Crossbreed een nieuw child
    cross("randomstart/output"+ str(win1) + ".txt", "randomstart/output" + str(win2) + ".txt", i)

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

experiment_name = 'dummy_demo'
if not os.path.exists(experiment_name):
    os.makedirs(experiment_name)

for i in range(100):
    with open("randomstart/output"+ str(i) + ".txt") as f:
        lines = f.readlines()
        with open("output.txt", "w") as f1:
            f1.writelines(lines)


    # initializes environment with ai player using random controller, playing against static enemy
    env = Environment(experiment_name=experiment_name, player_controller=player_controller())
    env.play()
    print("RESULT: ", i, env.fitness_single())

################################
# EvoMan FrameWork - V1.0 2016 #
# Author: Karine Miras         #
# karine.smiras@gmail.com      #
################################

# imports framework
import sys, os
sys.path.insert(0, 'evoman')
from environment import Environment

experiment_name = 'dummy_demo'
if not os.path.exists(experiment_name):
    os.makedirs(experiment_name)

# initializes environment with ai player using random controller, playing against static enemy
env = Environment(experiment_name=experiment_name)


# lijst meegeven aan environment (105 items  ipv 265) met cijfers die NN aanzet (= 1 player)
sol = np.loadtxt('solutions_demo/demo_all.txt')
env.play(sol)

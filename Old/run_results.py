import sys, os
sys.path.insert(0, 'evoman')
from environment import Environment
from ai_controller import player_controller
from operator import itemgetter
from smart_functions import *
import random
import matplotlib.pyplot as plt

index = 0

experiment_name = 'dummy_demo'
if not os.path.exists(experiment_name):
    os.makedirs(experiment_name)

import glob
import errno
path = '/Users/Julia/Dropbox/Master/Evolutionary computing/EvolutionaryComputing/bestresults/bestresultsDensitylevel1mutation0.01/*.txt'
files = glob.glob(path)

for file in files:

	index += 1
	f = open(file, "r")
	copy = open("output.txt", "w")
	for line in f:
	    copy.write(line)

# initializes environment with ai player using random controller, playing against static enemy
	env = Environment(experiment_name=experiment_name, player_controller=player_controller(), speed="fastest", enemies = [1])
	alle = env.play()

	with open("run/test.txt", "a") as txt_file:
		txt_file.write(str(index) + ": " + str(alle) + "\n")

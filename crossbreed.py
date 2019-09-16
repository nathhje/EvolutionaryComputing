import random
import numpy as np
experiment_name = 'dummy_demo'
from environment import Environment
from ai_controller import player_controller


def cross(array1, array2):
    child = []

    for i in range(len(array1)):
        if random.random() > 0.5:
            child.append(array1[i])
            #print(i)
        else:
            child.append(array2[i])

    return child


def pickparents(N, listscores):
    win1 = 0
    win2 = 0

    for i in [0]: #range(N):
        a = random.randint(0, N - 1)
        b = random.randint(0, N - 1)
        if listscores[a][1] > listscores[b][1]:
            win1 = a
        else:
            win1 = b

        a = random.randint(0, N - 1)
        b = random.randint(0, N - 1)
        if listscores[a][1] > listscores[b][1]:
            win2 = a
        else:
            win2 = b
    return (win1, win2)

def genrandomstart(N):
    alldata = []
    for i in range(N):
        data =  np.random.randint(2, size=(300, 6))
        alldata.append(data)
    return alldata

def fitnesscheck(data):

    with open("output.txt", "w") as txt_file:
        for line in data:
            txt_file.write(" ".join(str(line)) + "\n")

    # initializes environment with ai player using random controller, playing against static enemy
    env = Environment(experiment_name=experiment_name, player_controller=player_controller(), speed="fastest")
    env.play()

    return env.fitness_single()

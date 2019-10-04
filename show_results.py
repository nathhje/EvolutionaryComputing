################################
# EvoMan FrameWork - V1.0 2016 #
# Author: Karine Miras         #
# karine.smiras@gmail.com      #
################################

# imports framework
import random
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import copy
from scipy import stats

# GENERAL FUNCTIONS
def func_growth_results(parentchoice,enemy, mutation_rate):
    # open data from txt file
    growth_tournament = open_data("Tournament",enemy, mutation_rate)
    growth_density = open_data("Density",enemy, mutation_rate)

    # show the results
    # show_single_growth_results(growth_tournament)
    show_both_growth_results(growth_tournament, growth_density)

# def show_all_growth_results(dataset):
def all_growth_results():
    mutation = [0.005,0.01,0.015,0.02,0.025,0.03]
    level = [1,6,8]

    dataset = []
    for lev in level:
        tour_array = []
        density_array = []
        for mutate in mutation:
            print('mutation', mutate, 'level', lev)
            #func_growth_results(parentchoice='Tournament', enemy = lev, mutation_rate= mutate)
            growth_tournament = open_data("Tournament",lev, mutate)
            tour_array = tour_array + growth_tournament
            growth_density = open_data("Density",lev, mutate)
            density_array = density_array + growth_density

        show_both_growth_results(tour_array, density_array, lev)


def t_test_results(enemy, mutation_rate):
    # open data from txt file
    growth_tournament = open_data("Tournament",enemy, mutation_rate)
    growth_density = open_data("Density",enemy, mutation_rate)

    # show the results
    oldgrowth_tour = growth_tournament.copy()
    newgrowth_tour = list(map(list, zip(*oldgrowth_tour)))
    oldgrowth_dens = growth_density.copy()
    newgrowth_dens = list(map(list, zip(*oldgrowth_dens)))

    return stats.ttest_ind(newgrowth_dens[-1], newgrowth_tour[-1])

# OPEN DATA
def open_data(parentchoice,enemy, mutation_rate):
    # The growth results
    filename = "allgrowthresults/growthresults"+ parentchoice + "level"+ str(enemy) +"mutation"+ str(mutation_rate) +".txt"

    with open(filename, "r") as txt_file:
        results = txt_file.read().split('\n')

        if len(results) % 2 == 1:
            results.pop(-1)

        for i in range(len(results)):
            results[i] = results[i].strip("[").strip("]")
            results[i] = results[i].split(",")

            for j in range(len(results[i])):
                results[i][j] = float(results[i][j].strip())

    # make sure all generations contain values
    for generation in results:
        while len(generation) != 60: #number of generations
            generation.append(generation[-1])

    return results

# SHOW RESULTS
def show_single_growth_results(growth_results):
    # Shows both the mean, sd over time of either tournament or density
    oldgrowth = growth_results.copy()
    newgrowth = list(map(list, zip(*oldgrowth)))

    mean = []
    sd = []
    for step in newgrowth:
        mean.append(np.mean(step))
        sd.append(np.std(step))

    upperbound = [m + s for m, s in zip(mean, sd)]
    lowerbound = [m - s for m, s in zip(mean, sd)]

    # plot
    plt.plot(mean, label = "mean")
    plt.fill_between(range(len(mean)), upperbound, lowerbound, alpha = 0.1, label = "sd")
    plt.title('Growth of the fitness over the generations')
    plt.xlabel('Number of generation')
    plt.ylabel('Fitness')
    plt.ylim((0,100))
    plt.legend()
    plt.show()

def show_both_growth_results(growth_tournament, growth_density, lev = ""):
    # Shows both the mean, sd over time of tournament and density
    oldgrowth_tour = growth_tournament.copy()
    newgrowth_tour = list(map(list, zip(*oldgrowth_tour)))
    oldgrowth_dens = growth_density.copy()
    newgrowth_dens = list(map(list, zip(*oldgrowth_dens)))

    mean_tour = []
    sd_tour = []
    mean_dens = []
    sd_dens = []
    for step in newgrowth_tour:
        mean_tour.append(np.mean(step))
        sd_tour.append(np.std(step))
    for step in newgrowth_dens:
        mean_dens.append(np.mean(step))
        sd_dens.append(np.std(step))

    upperbound_tour = [m + s for m, s in zip(mean_tour, sd_tour)]
    lowerbound_tour = [m - s for m, s in zip(mean_tour, sd_tour)]
    upperbound_dens = [m + s for m, s in zip(mean_dens, sd_dens)]
    lowerbound_dens = [m - s for m, s in zip(mean_dens, sd_dens)]

    # plot
    plt.plot(mean_tour, label = "mean tournament")
    plt.plot(mean_dens, label = "mean fitness proportionate")
    plt.fill_between(range(len(mean_tour)), upperbound_tour, lowerbound_tour, alpha = 0.1, label = "sd tournament")
    plt.fill_between(range(len(mean_dens)), upperbound_dens, lowerbound_dens, alpha = 0.1, label = "sd fitness proportionate")
    plt.title('Growth of the fitness over the generations (level ' + str(lev) + ')')
    plt.xlabel('Number of generations')
    plt.ylabel('Fitness')
    plt.ylim((0,100))
    plt.legend()
    plt.show()


# Run the program
selection="Density" # Tournament or Density
m_rate= 0.015 # 0.005, 0.01, 0.015, 0.02, 0.025, 0.03
level = 8 # 1, 6, 8


#func_growth_results(parentchoice=selection, enemy = level, mutation_rate= m_rate)
all_growth_results()
# result = t_test_results(1, 0.005)
# print(result)

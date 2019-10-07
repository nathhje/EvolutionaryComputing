import numpy as np
import matplotlib.pyplot as plt

def open_data(file_path):
	with open(file_path, "r") as txt_file:
	    results = txt_file.read().split('\n')

	fitness_list = []
	p_life_list = []
	e_life_list = []
	time_list = []

	for result in results:
		result = result.split("(")
		fitness, p_life, e_life, time = result[1].strip(")").split(",")
		fitness_list.append(float(fitness))
		p_life_list.append(float(p_life))
		e_life_list.append(float(e_life))
		time_list.append(float(time))

	return(fitness_list, p_life_list, e_life_list, time_list)


def get_p_life(names_files):
	p_list = []

	for file in names_files:
		p_list = p_list + open_data(file)[1]

	return p_list



dens = ["run/Densitylevel1mutation0.005.txt","run/Densitylevel1mutation0.01.txt", "run/Densitylevel1mutation0.025.txt"]
tour = ["run/Tournamentlevel1mutation0.005.txt","run/Tournamentlevel1mutation0.01.txt","run/Tournamentlevel1mutation0.015.txt",
			"run/Tournamentlevel1mutation0.02.txt", "run/Tournamentlevel1mutation0.03.txt"]



p_dens = get_p_life(dens)
p_tour = get_p_life(tour)

print(np.mean(p_dens))
print(np.mean(p_tour))
print(np.std(p_dens))
print(np.std(p_tour))

fig, ax = plt.subplots()

ax.boxplot([p_dens,p_tour])
plt.title('Difference in player life in level 1 for algortihms in best results')
plt.xlabel('Algorithm')
plt.ylabel('Player life')
plt.xticks([1, 2], ['Fitness proportion', 'Tournement'])

plt.show()
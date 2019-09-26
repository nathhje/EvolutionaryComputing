import random
import numpy as np
experiment_name = 'dummy_demo'
from environment import Environment
from ai_controller import player_controller

# 1. Create the population
# 2. Determine fitness
# 3. Select the mating pool
# 4. Breed
# 5. Mutate
# 6. Repeat

# 1. Create the population
# population of the first generation
def initial_population(pop_size):
    population = []
    for i in range(pop_size):
        data =  np.random.randint(2, size=(300, 6))
        population.append(data)
    return population

# 2. Determine fitness
def fitnesscheck(data):

    with open("output.txt", "w") as txt_file:
        for line in data:
            txt_file.write(" ".join(str(line)) + "\n")

    # initializes environment with ai player using random controller, playing against static enemy
    env = Environment(experiment_name=experiment_name, player_controller=player_controller(), speed="fastest")
    env.play()

    return env.fitness_single()

# 3. Select the mating pool
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

        while True:
            a = random.randint(0, N - 1)
            b = random.randint(0, N - 1)
            if listscores[a][1] > listscores[b][1]:
                win2 = a
            else:
                win2 = b

            if win1 != win2:
                break
    return (win1, win2)

# 4. Breed
def cross(array1, array2):
    child1 = []
    child2 = []

    gene_number = len(array1)
    current_gene = len(child1)

    parent1 = array1
    parent2 = array2
    counter = 0

    while current_gene<gene_number:

        max_length = gene_number-current_gene

        inherit = random.randint(1,50)

        if inherit > max_length:
            inherit = max_length

        inheritance1 = parent1[current_gene:current_gene+inherit]
        inheritance2 = parent2[current_gene:current_gene+inherit]

        for row in inheritance1:

            child1.append(row)

        for row in inheritance2:
            child2.append(row)

        current_gene = len(child1)

        if counter%2==0:
            parent1 = array2
            parent2 = array1
        else:
            parent1 = array1
            parent2 = array2

        counter+=1


    return child1, child2

# 5. Mutate
def mutate(individual, mutation_rate):


    mutation_decision = random.randint(0, 100)

    # krijgt een individu een mutatie
    if mutation_decision < mutation_rate * 100:

        number_of_genes = 1500

        # hoeveel mutaties krijgt een individu
        mut_rate_calc = np.random.normal((number_of_genes * mutation_rate), 5, 1)

        # welke genen (regels) worden er aangepast
        which_genes = random.sample(range(300), mut_rate_calc)

        for gene in which_genes:

            # welke actie in het gen wordt aangepast
            which_action = random.randint(0,4)

            if individual[gene][which_action] == 0:
                individual[gene][which_action] = 1

            else:
                individual[gene][which_action] = 0

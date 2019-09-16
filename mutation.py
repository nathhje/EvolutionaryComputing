import random

def mutate(individual):
    number_of_mutations = 15

    which_genes = random.sample(range(len(individual)), number_of_mutations)

    for gene in which_genes:

        which_action = random.randint(0,5)
        
        if individual[gene][which_action] == 0:
            individual[gene][which_action] = 1

        else:
            individual[gene][which_action] = 0
        

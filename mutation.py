import random
import numpy as np

def mutate(individual, mutation_rate):


    mutation_decision = random.randint(0, 100)

    # krijgt een individu een mutatie
    if mutation_decision < mutation_rate * 100:

        number_of_genes = 1500

        # hoeveel mutaties krijgt een individu
        mut_rate_calc = np.random.normal((number_of_genes * mutation_rate), 5, 1)

        # welke genen (regels) worden er aangepast
        which_genes = random.sample(range(len(individual)), mut_rate_calc)

        for gene in which_genes:

            # welke actie in het gen wordt aangepast
            which_action = random.randint(0,4)
            
            if individual[gene][which_action] == 0:
                individual[gene][which_action] = 1

            else:
                individual[gene][which_action] = 0
        

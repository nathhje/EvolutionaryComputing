###################################
# EvoMan FrameWork - 2020         #
# Authors: Julia Anten,           #
# Jasper den Duijf, Romy Meester, #
# Nathalie van Sterkenburg        #
###################################

# imports framework
import matplotlib.pyplot as plt



# OPEN DATA
def open_data(filename):
    with open(filename, "r") as txt_file:
        results = txt_file.read().split('\n')

        if len(results) % 2 == 1:
            results.pop(-1)

        for i in range(len(results)):
            results[i] = results[i].strip("[").strip("]")
            results[i] = results[i].split(",")

            for j in range(len(results[i])):
                results[i][j] = float(results[i][j].strip())

    return results

def end_boxplot(level):
    mutation = [0.005,0.01,0.015,0.02,0.025,0.03]
    selection = ["Tournament","Density"]

    lastresult = []

    for select in selection:
        for mutate in mutation:

            lastresult.append([])

            filename = "growthresults/growthresults"+ select + "level"+ str(level) +"mutation"+ str(mutate) +".txt"

            result = open_data(filename)

            for row in result:
                lastresult[-1].append(row[-1])

    plt.figure()
    box1 = plt.boxplot(lastresult[0:6], positions = [4,9,14,19,24,29], widths = 1, patch_artist = True)
    #plt.setp(thebox['medians'],color = 'green')
    for element in ['boxes', 'whiskers', 'fliers', 'means', 'medians', 'caps']:
        plt.setp(box1[element], color='red')
    for patch in box1['boxes']:
        patch.set(facecolor='white')
    box2 = plt.boxplot(lastresult[6:12], positions = [5,10,15,20,25,30], widths = 1, patch_artist = True)
    #plt.setp(thebox['medians'],color = 'green')
    for element in ['boxes', 'whiskers', 'fliers', 'means', 'medians', 'caps']:
        plt.setp(box2[element], color='green')
    for patch in box2['boxes']:
        patch.set(facecolor='white')
    plt.xticks([5,10,15,20,25,30],['5','10','15','20','25','30'])
    plt.xlim(3,31)
    plt.legend([box1["boxes"][0], box2["boxes"][0]], ['tournament', 'fitness proportion'], loc='upper right')
    plt.xlabel(r"mutation rate ($10^{-3}$)")
    plt.ylabel("fitness score")
    plt.title("boxplot of the end results of level %i"%(level))
    plt.show()

def best_boxplot(level):
    mutation = [0.005,0.01,0.015,0.02,0.025,0.03]
    selection = ["Tournament","Density"]

    bestresult = []

    for select in selection:
        for mutate in mutation:

            bestresult.append([])

            filename = "growthresults/growthresults"+ select + "level"+ str(level) +"mutation"+ str(mutate) +".txt"

            result = open_data(filename)

            for row in result:
                bestresult[-1].append(max(row))

    plt.figure()
    box1 = plt.boxplot(bestresult[0:6], positions = [4,9,14,19,24,29], widths = 1, patch_artist = True)
    #plt.setp(thebox['medians'],color = 'green')
    for element in ['boxes', 'whiskers', 'fliers', 'means', 'medians', 'caps']:
        plt.setp(box1[element], color='red')
    for patch in box1['boxes']:
        patch.set(facecolor='white')
    box2 = plt.boxplot(bestresult[6:12], positions = [5,10,15,20,25,30], widths = 1, patch_artist = True)
    #plt.setp(thebox['medians'],color = 'green')
    for element in ['boxes', 'whiskers', 'fliers', 'means', 'medians', 'caps']:
        plt.setp(box2[element], color='green')
    for patch in box2['boxes']:
        patch.set(facecolor='white')
    plt.xticks([5,10,15,20,25,30],['5','10','15','20','25','30'])
    plt.xlim(3,31)
    plt.legend([box1["boxes"][0], box2["boxes"][0]], ['tournament', 'fitness proportion'], loc='upper right')
    plt.xlabel(r"mutation rate ($10^{-3}$)")
    plt.ylabel("fitness score")
    plt.title("boxplot of the best results of level %i"%(level))
    plt.show()

def best_end_boxplot(level):
    mutation = [0.005,0.01,0.015,0.02,0.025,0.03]
    selection = ["Tournament","Density"]

    lastresult = []
    bestresult = []

    for select in selection:
        for mutate in mutation:

            bestresult.append([])

            filename = "growthresults/growthresults"+ select + "level"+ str(level) +"mutation"+ str(mutate) +".txt"

            result = open_data(filename)

            for row in result:
                bestresult[-1].append(max(row))

    for select in selection:
        for mutate in mutation:

            lastresult.append([])

            filename = "growthresults/growthresults"+ select + "level"+ str(level) +"mutation"+ str(mutate) +".txt"

            result = open_data(filename)

            for row in result:
                lastresult[-1].append(row[-1])

    plt.figure()
    box1 = plt.boxplot(lastresult[0:6], positions = [4,9,14,19,24,29], widths = 1, patch_artist = True)
    #plt.setp(thebox['medians'],color = 'green')
    for element in ['boxes', 'whiskers', 'fliers', 'means', 'medians', 'caps']:
        plt.setp(box1[element], color='red')
    for patch in box1['boxes']:
        patch.set(facecolor='white')
    box2 = plt.boxplot(lastresult[6:12], positions = [5,10,15,20,25,30], widths = 1, patch_artist = True)
    #plt.setp(thebox['medians'],color = 'green')
    for element in ['boxes', 'whiskers', 'fliers', 'means', 'medians', 'caps']:
        plt.setp(box2[element], color='green')
    for patch in box2['boxes']:
        patch.set(facecolor='white')
    box3 = plt.boxplot(bestresult[0:6], positions = [4,9,14,19,24,29], widths = 1, patch_artist = True)
    #plt.setp(thebox['medians'],color = 'green')
    for element in ['boxes', 'whiskers', 'fliers', 'means', 'medians', 'caps']:
        plt.setp(box3[element], color='cyan')
    for patch in box3['boxes']:
        patch.set(facecolor='white')
    box4 = plt.boxplot(bestresult[6:12], positions = [5,10,15,20,25,30], widths = 1, patch_artist = True)
    #plt.setp(thebox['medians'],color = 'green')
    for element in ['boxes', 'whiskers', 'fliers', 'means', 'medians', 'caps']:
        plt.setp(box4[element], color='orange')
    for patch in box4['boxes']:
        patch.set(facecolor='white')
    plt.xticks([5,10,15,20,25,30],['5','10','15','20','25','30'])
    plt.xlim(3,31)
    plt.ylim(0,140)
    plt.legend([box1["boxes"][0], box2["boxes"][0], box3["boxes"][0], box4["boxes"][0]], ['tournament last', 'fitness proportion last', 'fitness proportion best', 'fitness proportion best'], loc='upper right')
    plt.xlabel(r"mutation rate ($10^{-3}$)")
    plt.ylabel("fitness score")
    plt.title("boxplot of the best and last results of level %i"%(level))
    plt.show()

# Run the program
enemy = 8 # 1, 6, 8

end_boxplot(enemy)
best_boxplot(enemy)
best_end_boxplot(enemy)

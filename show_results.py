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


def main(parentchoice,enemy, mutation_rate):
    # open data from txt file
    growth_results = open_data(parentchoice,enemy, mutation_rate)


    # show the results
    # show_all_growth_results(growth_results)
    # show_hist_growth_results()


# OPEN DATA
def open_data(parentchoice,enemy, mutation_rate):
    # The growth results
    growth_results = []
    with open("Final_results/growthresults/growthresults"+ parentchoice + "level"+ str(enemy) +"mutation"+ str(mutation_rate) +".txt", "r") as txt_file:
        results = txt_file.read().split('\n') #list

        for lines in results:
            print(type(lines))
            # print(lines)
        #     line = lines.split(" ").split("[").split("]")
        #     generation = list(line)
        #     growth_results.append(generation)
    #     #     print(line)
    # # print(len(lines))
    # print(lines)

    # for line in txt_file:
    #     newlist = [int(i) for i in line]
    #     growth_results.append(newlist)
    # print(type(results))
    # print(NEW)
    # print(growth_results[0])
    # print(growth_results[-1])
    return growth_results

# SHOW RESULTS
def show_all_growth_results(): #growth_results
    # The growth results over time
    for count, value in enumerate(data, 1):
        plt.plot(value, label = str(count))
        plt.title('Growth of the fitness over the generations')
        plt.xlabel('Number of generation')
        plt.ylabel('Fitness')
        plt.ylim((0,100))
        plt.legend()
    plt.show()

def show_hist_growth_results():
    # The histogram of the growth results
    # TO DO: FIX THE AXIS ZODAT ALLE RESULTATEN DEZELFDE ASSEN HEBBEN
    hist_growth = []
    for generation in data:
        hist_growth.append(generation[-1])

    plt.hist(hist_growth)
    plt.title('Histogram of generation growth' + selection + m_rate + level)
    plt.show()

def klad():
    sns.set(style="darkgrid")


    g = sns.jointplot("total_bill", "tip", data=tips, kind="reg",
                  xlim=(0, 60), ylim=(0, 12), color="m", height=7)

def plotss():
    # Timeseries plot with error bands
    d = pd.DataFrame(data)
    print(d)
    sns.lineplot(data = data)




# Run the program
if __name__ == '__main__':

    selection="Tournament" # Tournament or Density
    m_rate=0.005 # 0.005, 0.01, 0.015, 0.02, 0.025, 0.03
    level = 1 # 1, 6, 8

    # main(parentchoice=selection, enemy = level, mutation_rate= m_rate)

    data = [[9.720214626708028, 12.402528493096131, 12.414371371849523, 16.01357500503327, 20.971015634826983, 22.136871184578357, 27.758586825478364, 33.157305594949705, 35.62339327392489, 37.17300793313294, 37.87685950817044, 40.790368210598544, 43.514149170390375, 47.537660459039465, 46.67916719182411, 49.62160035753268, 49.19076399721417, 55.488303068356764, 53.47019094043301, 56.39027643336708, 57.97438190444035, 57.524775247564016, 61.84191699410119, 62.78453615662202, 63.37308573974715, 65.73765562724984, 66.86077765968066, 69.64786958156702, 72.65437310197584, 70.96542245619843, 73.95390883213852, 77.98307173612025, 78.10778245107025, 79.5803116861247, 77.07006257643361, 80.21932769948026, 81.44604523018477, 83.56758977871652, 84.50034414009414, 72.36842188753705, 68.09355175795898, 70.56881354045566, 73.04486067044239, 57.74564601793244, 59.09721671291253, 61.123263842899256, 61.12535810287271, 63.6006198853694, 64.95245236284617, 66.30245236284617, 66.75271414534285, 68.55297592783953, 70.12797592783953, 73.05297592783953, 74.62797592783953, 75.52797592783953, 75.30297592783953, 66.75297592783953, 66.75297592783953, 66.75297592783953], [5.666013216255642, 7.945724793936156, 9.090741874959344, 9.31936068026037, 12.903203774034031, 14.909217182761058, 14.932087875640656, 16.951184858902874, 15.824161611567934, 12.67874873647601, 16.9447671336736, 17.610276601786016, 14.942288245028013, 20.12001071715938, 21.487442269277942, 24.146735497186487, 28.212273717767424, 29.554599610788898, 31.3295038578483, 30.629781030383178, 32.433963107563194, 35.85484876031243, 37.865236871475716, 36.29569759399083, 39.224278574634496, 39.4681628963002, 41.27032480482909, 40.82932678052323, 43.09694330190446, 44.90447641918247, 45.567506184288526, 44.90318712753764, 45.78701659633826, 49.635009545178875, 50.9749920095507, 53.87811145544913, 54.79050818924564, 49.16674110258627, 52.30589942379396, 54.07658905902247, 53.63537379628848, 45.53967510658761, 50.70581512698643, 59.041744376772726, 62.201514225344944, 65.33352674616236, 64.83314388113737, 67.37507383243432, 67.37909176985393, 68.73144454818427, 70.08259041159286, 72.33259041159286, 73.23259041159287, 74.13259041159287, 75.70669517527544, 75.70669517527544, 75.25669517527544, 74.35848564791027, 75.25669517527544]]

    show_all_growth_results()
    # show_hist_growth_results()
    # plotss()

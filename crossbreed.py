import random

def cross(string1, string2, i):

    linearray1 = []
    linearray2 = []


    with open(string1) as f:
        lines = f.readlines()
        for line in lines:
            linearray1.append(line)

    with open(string2) as f:
        lines = f.readlines()
        for line in lines:
            linearray2.append(line)

    with open("secondfolder/child" + str(i) + ".txt", "w") as f1:
        for i in range(len(linearray1)):
            if random.random() > 0.5:
                f1.writelines(linearray1)
                #print(i)
            else:
                f1.writelines(linearray1)

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

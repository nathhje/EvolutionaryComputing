import numpy as np

for i in range(100):
    data =  np.random.randint(2, size=(300, 6))

    with open("randomstart/output"+ str(i) + ".txt", "w") as txt_file:
        for line in data:
            txt_file.write(" ".join(str(line)) + "\n") # works with any number of elements in a line

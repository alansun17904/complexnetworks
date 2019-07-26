import numpy as np
import random
f = open("../data/n.txt")

nn = f.readline()
n = int(nn)
startt = f.readline()
start = int(startt)    # first node that starts with

line = f.readline()
first_infection = line.split(",")
for i in range(len(first_infection)):
    first_infection[i] = int(first_infection[i])-start    # infection stores the newly infected nodes
print(first_infection)

run = f.readline()
runtime = run.split(",")
for i in range(len(runtime)):
    runtime[i] = int(runtime[i])

net = np.zeros((n, n))      # net stores the adjacency matrix

strlist = f.readlines()
for line in strlist:
    linelist = line.split(",")
    a = int(linelist[0])
    b = int(linelist[1])
    w = float(linelist[2])
    net[a-start][b-start] = w
    net[b-start][a-start] = w
"""
for i in range(n):
    for j in range(n):
        print(net[i][j],' ',end='')
    print()
"""

roundtime = 0
for roundtime in [0]:
    average = 0
    s = 0
    for k in range(100000):
        infection = first_infection[:]
        oldinfe, newinfe = infection[:], infection[:]

        while newinfe:
            oldinfe = newinfe[:]
            newinfe = []
            for i in oldinfe:
                rand = random.random()
                for j in range(n):
                    if (net[i][j] > 0) and (j not in infection) and (rand <= net[i][j]):
                        infection.append(j)
                        newinfe.append(j)
            # print(newinfe)

        s += len(infection)
    average = s / runtime[roundtime]
    proportion = average / n
    print(runtime[roundtime], "run average:", round(average, 3), "nodes infected, proportion =", round(proportion, 3))
    # How to eliminate the zero in the integer part?  ".04"
    print(runtime[roundtime], "run average:", average, "nodes infected, proportion =", proportion)
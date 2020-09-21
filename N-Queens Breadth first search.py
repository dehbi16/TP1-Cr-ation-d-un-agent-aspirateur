import numpy as np
import math

n = 4
nbsolution = 0

def positions(L):
    positionpossible = []
    for i in range(n):
        possible = True
        if i not in L:
            for j in range(len(L)):
                if abs(L[j]-i) == abs(len(L)-j):
                    possible = False
        else:
            possible = False
        if possible:
            positionpossible.append(i)
    return positionpossible

solution = [[i] for i in range(n)]
while len(solution) != 0:
    a = solution[0]
    del solution[0]
    if len(a) == n:
        nbsolution+=1
        print(a)
    else:
        position = positions(a)
        for i in range(len(position)):
            solution.append(a+[position[i]])

print(nbsolution)


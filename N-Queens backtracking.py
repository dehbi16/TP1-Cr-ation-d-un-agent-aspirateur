import numpy as np
import math

solution = []
nbsolution = 0


def solve(n, colonne):
    global nbsolution
    if len(solution) == n:
        print(solution)
        nbsolution += 1
    else:
        position = positions (n, colonne)
        for i in range (len(position)):
            solution.append(position[i])
            solve(n, colonne+1)
            solution.pop()

def positions(n, colonne):
    positionpossible = []

    for i in range(n):
        possible = True
        if i not in solution:
            for j in range(len(solution)):
                if abs(solution[j]-i) == abs(colonne-j):
                    possible = False
        else:
            possible = False
        if possible:
            positionpossible.append(i)
    return positionpossible

if __name__=='__main__':
    solve(10,0)
    print(nbsolution)

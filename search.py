import math
import random as rd
'''
O : vide
1 : poussière
2 : bijoux
3 : poussière + bijoux
4 : Robot
5 : Robot + poussière
6 : Robot + bijoux
7 : Robot + bijoux + poussière
'''
n = 5
environnement = [[0 for i in range(n)] for i in range(n)]

### Ajouter le robot
positionl = rd.randrange(0, n)
positionc = rd.randrange(0, n)
environnement[positionl][positionc] = 4

### Ajouter les poussières
for i in range(7):
    a = rd.randrange(0, n)
    b = rd.randrange(0, n)
    if environnement[a][b] == 4:
        environnement[a][b] = 5
    else:
        environnement[a][b] = 1

def positions(L):
    positionpossible = []


    return positionpossible

def clean():
    for i in range(n):
        for j in range(n):
            if environnement[i][j] == 1 or environnement[i][j] == 5:
                return False
    return True


solution = []
if positionc != 0: solution.append([0])
if positionl != 0: solution.append([1])
if positionl != n-1: solution.append([2])
if positionc != n-1: solution.append([3])

while len(solution) != 0:
    a = solution[0]
    del solution[0]
    if clean():
        print(a)
    else:
        position = positions(a)
print(environnement)
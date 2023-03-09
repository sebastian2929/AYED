# Sebastian David Blanco Rodriguez
# Cc: 1193219425
# carnet: 2171434
import collections
from sys import stdin


def colores():
    nodos = int(stdin.readline().strip())
    while nodos != 0:
        lim = int(stdin.readline().strip())
        grafo = [[0 for i in range(nodos)] for j in range(nodos)]
        color = [-1] * nodos
        for i in range(lim):
            nod1, nod2 = map(int, input().split())
            grafo[nod1][nod2] = 1
            grafo[nod2][nod1] = 1
        q = collections.deque([0])
        color[0] = 0
        bool = True
        while q:
            izquierda = q.popleft()
            for i in range(nodos):
                if not grafo[izquierda][i]:
                    continue
                if color[i] == -1:
                    color[i] = color[izquierda] + 1
                    q.append(i)

                elif color[izquierda] == color[i]:
                    bool = False

        if bool:
            print("BICOLORABLE.")
        else:
            print('NOT BICOLORABLE.')


colores()

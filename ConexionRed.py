# Sebastian David Blanco Rodriguez
# Cc: 1193219425
# carnet: 2171434

import sys

class UF:

    def __init__(self, N):
        self._id = list(range(N))
        self._count = N
        self._rank = [0] * N

    def find(self, p):
        id = self._id
        while p != id[p]:
            id[p] = id[id[p]]
            p = id[p]
        return p

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        id = self._id
        rank = self._rank

        i = self.find(p)
        j = self.find(q)
        if i == j:
            return

        self._count -= 1
        if rank[i] < rank[j]:
            id[i] = j
        elif rank[i] > rank[j]:
            id[j] = i
        else:
            id[j] = i
            rank[i] += 1

num_tests = int(input())


for t in range(num_tests):
    N = int(input())

    uf = UF(N + 1)
    num_connected = 0
    num_disconnected = 0

    queries = []

    line = stdin.readline().strip()
    while line != "":
        line = list(line.split())
        c = str(line[0])
        u = int(line[1])
        v = int(line[2])
        if c == "c":
            uf.union(u, v)
        else:
            queries.append(line)
            if uf.connected(u, v):
                num_connected += 1
            else:
                num_disconnected += 1
        try:
            line = stdin.readline().strip()
        except(EOFError):
            break

    if t > 0:
        stdout.write("\n")
    stdout.write("{},{}\n".format(num_connected, num_disconnected))


"""
Cristian David Naranjo Orjuela
Sebastian David Blanco Rodriguez
"""


def main():
    M = int(input("Digite el valor: "))
    N = int(input("Digite el valor: "))
    calculate = MCD(M, N)
    print(calculate)


def MCD(M, N):
    if N > M:
        return MCD(M, N)
    if N == 0:
        return M
    else:
        return MCD(N, N % M)


main()
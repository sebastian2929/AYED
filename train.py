"""
Sebastian David Blanco Rodriguez
"""


def main():
    train = int(input())
    for c in range(train):
        n = int(input())
        matriz = list(map(int, input().split()))
        index = 0
        for i in range(n):
            for j in range(i + 1, n):
                if matriz[i] > matriz[j]:
                    matriz[i], matriz[j] = matriz[j], matriz[i]
                    index += 1

        print("Optimal train swapping takes " + str(index) + " swaps.")


main()
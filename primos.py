"""
Sebastian David Blanco Rodriguez
"""
from sys import stdin


def main():
    num = int(stdin.readline())
    matriz = []
    while num > 0:
        output = primos(num)
        if output:
            matriz.append(num)
        num -= 1
    print(*matriz)


def primos(num):

    cont = 0
    for i in range(1,num+1):
        if num % i == 0:
            cont += 1
    if cont == 2:
        return True
    else:
        return False


main()

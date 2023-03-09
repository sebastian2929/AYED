"""
Sebastian David Blanco Rodriguez
"""
from sys import stdin


def main():
    nums = stdin.readline().split()
    while nums:
        i = int(nums[0])
        j = int(nums[1])
        sol = solution(i, j)
        print(str(i), str(j), sol)
        nums = stdin.readline().split()


def solution(i, j):
    operation = 1
    for n in range(i, j + 1):
        cont = 1
        while n != 1:
            if n % 2 == 0:
                n = n / 2
            else:
                n = (3 * n) + 1
            cont += 1
        operation = max(operation, cont)
    return operation


main()

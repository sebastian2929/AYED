"""
Sebastian David Blanco Roddriguez
"""
from sys import stdin


def super_digit():
    nums = stdin.readline().split()
    while nums:
        num = nums[0]
        plus = int(nums[1])
        suma = base(num, plus)
        output = sum(suma)
        print(output)
        nums = stdin.readline().split()


def sum(suma):
    suma = int(suma)
    if suma < 10:
        return suma
    else:
        suma = suma % 10 + sum(suma//10)
        return sum(suma)


def base(num, plus):
    cont = 1
    temp = num
    if plus != 1:
        while cont != plus:
            num += temp
            cont += 1
        return num


super_digit()

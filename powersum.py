"""
Sebastian David Blanco Rodriguez
"""


def main():
    x = int(input())
    n = int(input())
    output = recurrencia(x, n, 1)
    print(output)


def recurrencia(x, n, launch):
    index = 0
    for i in range(launch, x):
        solution = x - i ** n
        if solution == 0:
            index += 1
        if solution > 0:
            index += recurrencia(solution, n, i + 1)
        if solution < 0:
            continue
    return index


main()

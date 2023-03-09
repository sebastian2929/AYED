"""
Sebastian David Blanco Rodriguez
Cristian David Naranjo Orjuela
"""


def main():
    entero = int(input(""))
    final = binario(entero)
    print(final)


def binario(entero):
    return "" if entero <= 0 else str(entero % 2) + binario(entero//2)


main()

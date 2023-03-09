"""
Sebastian David Blanco Rodriguez
Cristian David Naranjo Orjuela
"""


def main():
    array = [1,2,3,4,5]
    n = 0
    print(array)
    inver = sort_array(array, n)
    print(inver)


def sort_array(array, n):
    if n == len(array):
        return array
    else:
        array[n] = array[n][::-1]
        n += 1
        return sort_array(array, str(n))


main()
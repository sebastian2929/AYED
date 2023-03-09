"""
Sebastian David Blanco Rodriguez
"""


def main():
    case = int(input())
    for i in range(case):
        line = input().split(" ")
        line = [int(i) for i in line]
        a = line[0]
        b = line[1]
        if a > b:
            print(">")
        elif a < b:
            print("<")
        else:
            print("=")


main()

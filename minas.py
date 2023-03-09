"""
sebastian david blanco rodriguez
"""


###
def main():
    index = 1
    output = []
    stop = 1
    while stop == 1:
        size = input("").split(" ")
        if size == ['0', '0']:
            stop = 0
        if size != ['0', '0']:
            size = [int(i) for i in size]
            rows = size[0]
            columns = size[1]
            matriz = board(rows)
            final = numbers(matriz, rows, columns)
            if index == 1:
                output.append(["Field #" + str(index) + ":"])
                for i in range(len(final)):
                    output.append(final[i])
            if rows >= 1 and columns >= 1 and index > 1:
                output.append("")
                output.append(["Field #" + str(index) + ":"])
                for i in range(len(final)):
                    output.append(final[i])
            index += 1
    for i in range(len(output)):
        print(*output[i])


def board(rows):
    matriz = []
    for i in range(rows):
        var = input("")
        var = " ".join(var[i:i + 1] for i in range(0, len(var), 1))
        within = var.split(" ")
        matriz.append(within)

    return matriz


def numbers(matriz, rows, columns):
    for i in range(rows):
        for j in range(columns):
            if matriz[i][j] == ".":
                matriz[i][j] = 0
    for i in range(rows):
        for j in range(columns):
            if matriz[i][j] == "*":
                for k in [-1, 0, 1]:
                    for h in [-1, 0, 1]:
                        if 0 <= i + k <= rows - 1 and 0 <= j + h <= columns - 1:
                            if matriz[i + k][j + h] != "*":
                                matriz[i + k][j + h] += 1
    return matriz


main()

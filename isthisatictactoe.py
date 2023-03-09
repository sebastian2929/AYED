"""
Sebastian David Blanco Rodriguez
"""


def main():
    case = int(input())
    index = 1
    m_temp = []
    output = []
    while index <= case:
        stop = True
        while stop:
            line = input("").split(" ")
            if line != ['']:
                matriz = table(line)
                m_temp.append(matriz)
                if len(m_temp) == 3:
                    result = check(m_temp)
                    output.append(result)
            if line == ['']:
                index += 1
                m_temp = []
                stop = False
    for i in range(len(output)):
        print(output[i])


def table(line):
    matriz = []
    for i in range(len(line[0])):
        matriz.append(line[0][i])
    return matriz


def check(m_temp):
    cont_x = 0
    cont_o = 0
    for i in range(len(m_temp)):
        for j in range(len(m_temp[0])):
            if m_temp[i][j] == "X":
                cont_x += 1
            if m_temp[i][j] == "O":
                cont_o += 1
    if cont_x - cont_o == 0 or cont_x - cont_o == 1:
        if m_temp[0][0] == "X" and m_temp[1][1] == "X" and m_temp[2][2] == "X":
            return "yes"
        if m_temp[0][0] == "O" and m_temp[1][1] == "O" and m_temp[2][2] == "O":
            return "yes"
        if m_temp[0][2] == "X" and m_temp[1][1] == "X" and m_temp[2][0] == "X":
            return "yes"
        if m_temp[0][2] == "O" and m_temp[1][1] == "O" and m_temp[2][0] == "O":
            return "yes"
        for i in range(len(m_temp)):
            if m_temp[i][0] == "X" and m_temp[i][1] == "X" and m_temp[i][1] == "X":
                return "yes"
            if m_temp[i][0] == "O" and m_temp[i][1] == "O" and m_temp[i][1] == "O":
                return "yes"
            for j in range(len(m_temp)):
                if m_temp[0][j] == "X" and m_temp[1][j] == "X" and m_temp[2][j] == "x":
                    return "yes"
                if m_temp[0][j] == "O" and m_temp[1][j] == "O" and m_temp[2][j] == "O":
                    return "yes"
    return "no"


main()

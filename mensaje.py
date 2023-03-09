"""
Sebastian David Blanco Rodriguez
"""


def main():
    case = int(input())
    print("")
    matriz = []
    output = []
    index = 1
    while index <= case:
        stop = True
        while stop:
            sentence = input("").split(" ")

            if sentence != ['']:
                words = translator(sentence)
                matriz.append(words)

            if sentence == ['']:
                matriz.append(" ")
                output.append("Case #" + str(index) + ":")
                for i in range(len(matriz)):
                    output.append(matriz[i])
                index += 1
                matriz = []
                stop = False

    for i in range(len(output)):
        print(output[i])


#
def translator(sentence):
    index = 0
    word_final = ""
    variable = len(sentence)
    letter = 1
    while index < variable:
        for i in range(variable):
            if len(sentence[i]) > letter:
                word = sentence[i]
                word_final += word[index]
                index += 1
                if len(sentence[i]) < i:
                    letter += 1
            if len(sentence[i]) <= letter:
                variable -= 1
    return word_final


#
main()

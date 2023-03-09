from sys import stdin


def notas():
    nombre = True
    while nombre:
        nombre = stdin.readline().strip()
        if nombre:
            print("NOTA PRIMER CORTE")
            nota1 = int(stdin.readline())
            print("NOTA SEGUNDO CORTE")
            nota2 = int(stdin.readline())
            print("NOTA TERCER CORTE")
            nota3 = int(stdin.readline())
            if nombre == "vecto":
                print("NOTA LABORATORIOS")
                notal = int(stdin.readline())
                notaf = (nota1 * 0.27) + (nota2 * 0.27) + (notal * 0.1) + (nota3 * 0.36)
            else:
                notaf = (nota1 * 0.3) + (nota2 * 0.3) + (nota3 * 0.4)
            print("MATERIA: " + nombre + "   " + "NOTA FINAL: " + str(notaf))
            print("-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-")



notas()
# Sebastian David Blanco Rodriguez
# Cc: 1193219425
# carnet: 2171434

from sys import stdin


class max(object):
    def __init__(self):
        self.__a = list()
        self.__size = 0

    def __len__(self):
        return self.__size

    def add(self, num):
        self.__a.append(num)
        self.__size += 1

    def mayor(self):
        self.__may = 0
        for i in range(self.__len__()):
            if self.__may < self.__a[i][0]:
                self.__may = self.__a[i][0]

    def consulm(self):
        return self.__may

    def queue(self):
        if self.__a[0][0] < self.__may:
            self.__a.append(self.__a[0]);
            del self.__a[0]
            self.queue()

    def remove_m(self):
        assert self.__size > 0
        del self.__a[0]
        self.__size -= 1

    def verificar(self):
        if self.__a[0][1] == True:
            return True
        else:
            return False

    def consul(self):
        return self.__a

def solve(n, pior, A):
    var = max()
    for i in range(len(A)):
        if i == pior:
            var.add([A[i], True])
        else:
            var.add([A[i], False])
    var2, index = False, 0
    while var2 == False:
        var.mayor()
        var.queue()
        var2 = var.verificar()
        if var2 == True:
            break
        else:
            var.remove_m()
        index += 1
    return index + 1


def main():
    case = int(stdin.readline())
    while case != 0:
        pre = [int(i) for i in stdin.readline().strip().split()]
        n, sol = pre[0], pre[1]
        lista = [int(j) for j in stdin.readline().strip().split()]
        print(solve(n, sol, lista))
        case -= 1


main()

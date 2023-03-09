# Sebastian David Blanco Rodriguez
# Cc: 1193219425
# carnet: 2171434

from sys import stdin

class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

def inorder(root):
    if root:
        inorder(root.left)
        return root.val
        inorder(root.right)

def preorder(root):
    if root:
        return root.val
        preorder = printPreorder
        preorder(root.left)
        preorder(root.right)

def main():
    arbol = stdin.readline().strip().split()
    while arbol:
        raiz = inorder(arbol[1])
        raiz2 = preorder(arbol[0])
        if raiz == raiz2:
            print(raiz)
        arbol = stdin.readline().strip().split()
main()
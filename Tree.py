import math
import operator
import time
import timeit
import random


class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            tmp = BinaryTree(newNode)
            tmp.leftChild = self.leftChild
            self.leftChild = tmp  # fa scorrere tutto il sottoalbero

    def insertRight(self, key):
        if self.rightChild is None:
            self.rightChild = BinaryTree(key)
        else:
            tmp = BinaryTree(key)
            tmp.rightChild = self.rightChild
            self.rightChild = tmp

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootKey(self, key):
        self.key = key

    def getRootVal(self):
        return self.key

    def preOrder(self, root):
        if root is not None:
            print(root.getRootVal())
            self.preOrder(root.getLeftChild())
            self.preOrder(root.getRightChild())

    def postOrder(self, root):
        if root is not None:
            self.postOrder(root.getLeftChild())
            self.postOrder(root.getRightChild())
            print(root.getRootVal())

    def postOrderVal(self, tree):
        opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        res1 = None
        res2 = None
        if tree:
            res1 = self.postOrderVal(tree.getLeftChild)
            res2 = self.postOrderVal(tree.getRightChild)
            if res1 and res2:
                return opers[tree.getRootVal()](res1, res2)
            else:
                return tree.getRootVal  # cazzo fa sta roba

    def Es2RicercaRicorsiva(self, value):
        found = False

        if value == self.key:
            found = True
            return found
        else:
            self.Es2RicercaRicorsiva(self.leftChild)
            self.Es2RicercaRicorsiva(self.rightChild)  # correggere da far stoppare

    def Es3SizeRicorsiva(self, count, tree):
        while self.key is not None:
            count += 1
            self.Es3SizeRicorsiva(count, self.getLeftChild)
            self.Es3SizeRicorsiva(count, self.getRightChild)
        return count


def inOrder(root):
    if root is not None:
        inOrder(root.getLeftChild())
        print(root.getRootVal())
        inOrder(root.getRightChild)


def conta_nodi(radice):
    if radice is None:
        return 0
    else:
        return 1 + conta_nodi(radice.leftChild) + conta_nodi(radice.rightChild)


def conta_nody(radice):
    if radice is None:
        return 0

    queue = [radice]
    numero_nodi = 0

    while queue:
        nodo = queue.pop(0)
        numero_nodi += 1

        if nodo.leftChild:
            queue.append(nodo.leftChild)

        if nodo.destro:
            queue.append(nodo.rightChild)

    return numero_nodi


r = BinaryTree('a')
print(r.getRootVal())
print(r.getLeftChild())
r.insertLeft('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())
r.insertRight('c')
print(r.getRightChild())
print(r.getRightChild().getRootVal())
r.getRightChild().setRootKey('hello')
print(r.getRightChild().getRootVal())
print(r.Es2RicercaRicorsiva('a'))

radice = BinaryTree(1)
radice.leftChild = BinaryTree(2)
radice.rightChild = BinaryTree(3)
radice.leftChild.leftChild = BinaryTree(4)
numero_nodi = conta_nodi(radice)
print("Il numero di nodi nell'albero binario è:", numero_nodi)

import math
import operator
import time
import timeit
import random

# This is a sample Python script.
import random


# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def CrazyTree(r):
    return [r, [], []]


def insertLeft(root, newBranch):
    t = root.pop(1)  # toglie figlio sinistro
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])  # ricordiamo che fa lo shift di tutto
    else:
        root.insert(1, [newBranch, [], []])
    return root


def insertRight(root, newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    return root


class BinaryTree:  # classe ricorsiva per questo si usano tutte le volte i cost
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key


def Es3SizeRicorsiva(tree):
    if tree is None:
        return 0
    return 1 + Es3SizeRicorsiva(tree.getLeftChild() + Es3SizeRicorsiva(tree.getRightChild()))


def iterativePreorder(root):
    if not root:
        return []
    stack = [root]
    result = []
    while stack:
        node = stack.pop()
        result.append(node.key)
        if node.rightChild:
            stack.append(node.rightChild)
        if node.leftChild:
            stack.append(node.leftChild)
    return result


def iterativeInorder(tree):
    if not tree:
        return []
    stack = []
    result = []
    current = tree
    while True:
        if current:
            stack.append(current)
            current = current.leftChild
        elif stack:
            current = stack.pop()
            result.append(current.key)
            current = current.rightChild
        else:
            break

    return result


def iterativePostOrder(tree):
    stack = []
    result = []
    if tree:
        stack.append(tree)

    while stack:
        node = stack.pop()
        result.append(node.key)

        if node.leftChild:
            stack.append(node.leftChild)
        if node.rightChild:
            stack.append(node.rightChild)

    return result[::-1]


def postorder(tree):
    if tree is not None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())


def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())


def inorder(tree):
    if tree is not None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())


def height7(tree):
    if tree is None:
        return 0
    return 1 + max(height7(tree.getLeftChild()), height7(tree.getRightChild()))


def Es2RicercaRicorsiva(tree, value):
    if tree is None:
        return False
    if value == tree.key:
        return True
    Es2RicercaRicorsiva(tree.getLeftChild(), value) or Es2RicercaRicorsiva(tree.getRightChild(), value)


def es8Function(tree):  # non è lineare
    if height7(tree) > 1:
        print(tree.key)
    if tree is not None:
        es8Function(tree.getLeftChild())
        es8Function(tree.getRightChild())


def es8FuncLine(tree):
    if tree is None:
        return 0
    temp = 1 + max(height7(tree.getLeftChild()), height7(tree.getRightChild()))
    if temp > 6:
        print(tree.key)
    return temp


def es9Function(tree):  # ?
    if not tree:
        return []
    stack = [tree]
    result = []
    while stack:
        node = stack.pop()
        result.append(node.key)
        if node.rightChild and height7(node.rightChild) > 2:
            stack.append(node.rightChild)
        if node.leftChild and height7(node.leftChild) > 2:
            stack.append(node.leftChild)
    return result


def ES9Prof(tree, originalTree):  # non lin
    if es8FuncLine(tree) == livello(originalTree, tree.key):
        print(tree.key)
    ES9Prof(tree.getLeftChild(), originalTree)
    ES9Prof(tree.getRightChild(), originalTree)


def livello(tree, x):
    # restituisce il livello di x nell'albero tree, -1 altrimneti
    if tree is None:
        return -1
    temp = livello(tree.getLeftChild(), x)
    if tree.key is x:
        return 0
    if temp != -1:
        return 1 + temp
    temp = livello(tree.getRightChild(), x)
    if temp != 1:
        return 1 + temp
    return -1


r = BinaryTree('a')
r.insertLeft('b')
r.insertRight('c')
r.insertLeft('d')
r.insertLeft('e')
r.getLeftChild().insertRight('f')
print(es9Function(r))

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

    def Es2RicercaRicorsiva(self, tree, value):
        found = False
        if value == self.key:
            found = True
            return found
        elif tree.getLeftChild() is not None:
            a = self.Es2RicercaRicorsiva(self.leftChild)
        elif tree.getRightChild() is not None:
            a = self.Es2RicercaRicorsiva(self.rightChild)  # correggere da far stoppare

    def Es3SizeRicorsiva(self):
        count = 1
        if self.leftChild:
            count += self.leftChild.Es3SizeRicorsiva()
        if self.rightChild:
            count += self.rightChild.Es3SizeRicorsiva()
        return count


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


def height(tree):
    if tree is None:
        return 0
    return 1 + max(height(tree.getLeftChild()), height(tree.getRightChild()))


def es8Function(tree):
    if height(tree) > 1:
        print(tree.key)
    if tree is not None:
        es8Function(tree.getLeftChild())
        es8Function(tree.getRightChild())


def es9Function(tree):
    if not tree:
        return []
    stack = [tree]
    result = []
    while stack:
        node = stack.pop()
        result.append(node.key)
        if node.rightChild and height(node.rightChild) > 2:
            stack.append(node.rightChild)
        if node.leftChild and height(node.leftChild) > 2:
            stack.append(node.leftChild)
    return result


r = BinaryTree('a')
r.insertLeft('b')
r.insertRight('c')
r.insertLeft('d')
r.insertLeft('e')
r.getLeftChild().insertRight('f')
print(es9Function(r))

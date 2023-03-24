import math
import time
import timeit
import random


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def getNext(self):
        return self.next

    def setNext(self, node):
        self.next = node


class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self, node):
        tmp = Node(node)
        tmp.setNext(self.head)
        self.head = tmp

    def size(self):
        tmp = self.head
        count = 0
        while tmp is not None:
            count += 1
            tmp = tmp.getNext()
        return count

    def search(self, item):
        tmp = self.head
        found = False
        while tmp is not None and found is False:
            if tmp.getData() == item:
                found = True
            else:
                tmp = tmp.getNext()
        return found

    def remove(self, item):  # TODO fa cacare non funziona rifallo
        found = False
        tmp = self.head
        previous = None
        while found is False:
            if tmp.getData == item:
                found = True
            else:
                tmp = tmp.getNext()

            if previous is None:
                self.head = tmp.getNext()
            else:
                previous.setNext(tmp.getNext())

    def Es1ReversePrint(self):  # si occhio che qui si va all'incontrario
        tmp = self.head
        arr = []
        while tmp is not None:
            arr.append(tmp.getData())
            tmp = tmp.getNext()

        for i in reversed(arr):
            print(i)

    def ES1Prof(self, list):
        if list:
            self.ES1Prof(list.getNext())
            print(list.head.getData())





myList = LinkedList()
myList.add(20)
myList.add(30)
myList.add(40)
myList.add(50)
myList.add(60)
print(myList.search(20))
print(myList.size())
myList.Es1ReversePrint()

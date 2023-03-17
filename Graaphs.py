class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}  # dizionario

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight  # dizion non ordinato

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex  # bo fa cacare come cosa

    def getVertex(self, key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None

    def __contains__(self, item):
        print('porcodio')
        return item in self.vertList  # override metoo base

    def addEdge(self, f, t, cost=0):  # mette i pesi e se uno non esiste lo crea
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


g = Graph()
for i in range(6):
    g.addVertex(i)

g.addEdge(0, 1, 5)
g.addEdge(0, 5, 2)
g.addEdge(1, 2, 4)
g.addEdge(2, 3, 9)
g.addEdge(3, 4, 7)
g.addEdge(3, 5, 3)
g.addEdge(4, 0, 1)
g.addEdge(5, 4, 8)
g.addEdge(5, 2, 1)

print(g.__contains__(1))  # figo rende true, non dovrebbe rendere l'item?

for v in g:
    for w in v.getConnections():
        print("( %s , %s )" % (v.getId(), w.getId()))

alfabeto = {1: "a", 2: "b", 3: "c", 4: "d"}

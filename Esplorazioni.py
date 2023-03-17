from pythonds.graphs import Graph, Vertex
from pythonds.basic import Queue
from pythonds.graphs import Graph


def bfs(g, start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)  # inserimento
    while vertQueue.size() > 0:
        currentVert = vertQueue.dequeue()  # pop item
        for nbr in currentVert.getConnections():  # scoore vicini in connessioni
            if nbr.getColor() == 'white':  # inizializzato di base a white
                nbr.setColor('gray')  # nodo esplorato messo a grey
                nbr.setDistance(currentVert.getDistance() + 1)  # dist = 0 default
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')


def traverse(y):
    x = y
    while x.getPred():
        print(x.getId())
        x = x.getPred()
    print(x.getId())


class DFSGraph(Graph):
    def __iter__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPredecessor(-1)  # TODO what
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)

    def dfsvisit(self, startVertex):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)  # semplicemente prende il tempo
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)

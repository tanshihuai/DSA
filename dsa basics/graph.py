class queue:
    def __init__(self):
        self.list = []

    def enqueue(self, item):
        self.list.append(item)

    def dequeue(self):
        return self.list.pop(0)

    def isEmpty(self):
        if len(self.list) == 0:
            return True
        return False


class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        else:
            self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def bfs(self, vertex):
        visited = set()
        q = queue()
        q.enqueue(vertex)
        while not q.isEmpty():
            current = q.dequeue()
            print(current)
            for i in self.gdict.get(current):
                if i not in visited:
                    visited.add(i)
                    q.enqueue(i)



d = {'a': ['b', 'c'],
     'b': ['a', 'd', 'e'],
     'c': ['a', 'e'],
     'd': ['b', 'e', 'f'],
     'e': ['b', 'c', 'd', 'f'],
     'f': ['d', 'e']
}

g = Graph(d)
g.bfs('a')
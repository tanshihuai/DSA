from collections import defaultdict

class queue:
    def __init__(self):
        self.data = []

    def enqueue(self, data):
        self.data.append(data)

    def dequeue(self):
        return self.data.pop(0)

    def notEmpty(self):
        if len(self.data) != 0:
            return True
        return False

class stack:
    def __init__(self):
        self.data = []

    def push(self, data):
        self.data.insert(0, data)

    def pop(self):
        return self.data.pop(0)

    def notEmpty(self):
        if len(self.data) != 0:
            return True
        return False


class graph:
    def __init__(self, dict):
        self.dict = dict

    def addEdge(self, vertex, edge):
        self.dict[vertex].append(edge)

    def bfs(self, vertex):
        if not vertex:
            return
        else:
            q = queue()
            q.enqueue(vertex)
            visited = set()
            visited.add(vertex)
            while q.notEmpty():
                current = q.dequeue()
                print(current)
                for i in self.dict[current]:
                    if i not in visited:
                        visited.add(i)
                        q.enqueue(i)

    def dfs(self, vertex):
        if not vertex:
            return
        else:
            s = stack()
            s.push(vertex)
            visited = set()
            visited.add(vertex)
            while s.notEmpty():
                current = s.pop()
                print(current)
                for i in self.dict[current]:
                    if i not in visited:
                        s.push(i)
                        visited.add(i)


    def topologicalsort(self):

        def arrange(visited, stack, vertex):
                visited.add(vertex)
                if self.dict.get(vertex) is not None:
                    for j in self.dict[vertex]:
                        if j not in visited:
                            arrange(visited, s, j)
                stack.push(vertex)

        visited = set()
        s = stack()

        for i in self.dict:
            if i not in visited:
                arrange(visited, s, i)
        print(s.data)


    def single_source_shortest_path(self, start, end):
        q = queue()
        q.enqueue([start])
        while q.notEmpty():
            path = q.dequeue()
            vertex = path[-1]
            if vertex == end:
                return path
            if self.dict.get(vertex):
                for i in self.dict[vertex]:
                    copy = path[:]
                    copy.append(i)
                    q.enqueue(copy)





g = {
    "a": ["b", "c"],
    "b": ["d", 'g'],
    "c": ["d", 'e'],
    "d": ["f"],
    "e": ['f'],
    "g": ["f"]
}

############################################ where he used new method to create graph ############################################

class graph2:

    def __init__(self):
        self.nodes = set()
        self.data = defaultdict(list)   # (list) means value is a list
        self.distance = {}

    def addNode(self, vertex):
        self.nodes.add(vertex)

    def addEdge(self, node1, node2, distance):
        self.data[node1].append(node2)
        self.distance[(node1, node2)] = distance

    # gave up learning
    # def dijkstra(self)



g1 = graph2()
g1.addEdge("a", "b", 2)
g1.addEdge("a", "c", 5)
g1.addEdge("b", "c", 6)
g1.addEdge("b", "d", 1)
g1.addEdge("b", "e", 3)
g1.addEdge("c", "f", 8)
g1.addEdge("d", "e", 4)
g1.addEdge("e", "g", 9)
g1.addEdge("f", "g", 7)



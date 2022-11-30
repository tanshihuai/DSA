class graph:
    def __init__(self, dict):
        self.dict = dict

    def addEdge(self, vertex, edge):
        self.dict[vertex].append(edge)


g = {
    "a": ["b", "c"],
    "b": ["a", "d", "e"],
    "c": ["a", "e"],
    "d": ["b", "e", "f"],
    "e": ["b", "c", "d", "f"],
    "f": ["d", "e"]
}

g1 = graph(g)
print(g1.dict)
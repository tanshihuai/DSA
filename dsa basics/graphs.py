from collections import defaultdict

class stack:
    def __init__(self):
        self.data = []

    def push(self, data):
        self.data.insert(0, data)

    def pop(self):
        return self.data.pop(0)


class graph:
    def __init__(self):
        self.graph = defaultdict(list)
        #         key : value
        #      string : list
        #      string : list
        #      string : list
        #      string : list


    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)




    def topologicalSort(self):

        def findleaf(stack, visited, vertex):
            if vertex not in visited:
                visited.add(vertex)
                if self.graph[vertex]:  # if key is pointing to something
                    for j in self.graph[vertex]:
                        findleaf(stack, visited, j)
                stack.push(vertex)

        s = stack()
        visited = set()

        for i in list(self.graph):      # u need the list because it is a default dict,
            findleaf(s, visited, i)     # otherwise when u vist vertexes that is not a key it will create a new key and change the size of the dict
        print(s.data)

g = graph()
g.addEdge("A", "C")
g.addEdge("C", "E")
g.addEdge("E", "H")
g.addEdge("E", "F")
g.addEdge("F", "G")
g.addEdge("B", "C")
g.addEdge("B", "D")
g.addEdge("D", "F")

g.topologicalSort()


# dictionary changed size during runtime when using defaultdict
# solution = u are probably iterating through the dictionary keys. you need to turn keys into a list first then iterate thru them,
# otherwise when u vist values that is not a key it will create a new key and change the size of the dict
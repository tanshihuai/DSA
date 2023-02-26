"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        # add to adj list
        # start dfs from adj list
        # add node into visited when visited
        # return when visiting visited node

        def dfs(node, adjlist, clone):
            if node in clone:
                return
            clone[node] = []
            for i in adjlist[node]:
                clone[node].append(i.val)
                dfs(i, adjlist, clone)

        adjlist = {}
        for i in range(len(node)):
            adjlist[i+1] = node[i]

        clone = {}
        for i in adjlist:
            dfs(i, adjlist, clone)

        return clone






adjList = [[2,4],[1,3],[2,4],[1,3]]
s = Solution()
s.cloneGraph(adjList)
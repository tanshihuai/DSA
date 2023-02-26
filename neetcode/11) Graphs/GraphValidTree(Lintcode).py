class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    via lintcode, not no full testcases
    """
    def valid_tree(self, n, edges):
        # write your code here
        map = {}
        visited = set()

        if not edges:
            return True

        def dfs(node):
            if node in visited:
                return False
            visited.add(node)
            if map.get(node):
                for i in map[node]:
                    return dfs(i)
            return True


        for i in edges:
            if map.get(i[0]):
                map[i[0]].append(i[1])
            else:
                map[i[0]] = [i[1]]

        x = dfs(edges[0][0])
        y = len(visited) == n
        return x and y





n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
s = Solution()
print(s.valid_tree(n,edges))

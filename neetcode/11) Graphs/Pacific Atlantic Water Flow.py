class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(heights)
        cols = len(heights[0])
        pac_visited = set()
        alt_visited = set()
        ans = []

        def dfs(row, col, visited, prev_height, heights):
            # find which one leads to row, col
            if (row, col) in visited:
                return
            if row < 0 or col < 0 or row >= rows or col >= cols:
                return
            if heights[row][col] < prev_height:
                return
            else:
                visited.add((row, col))
                dfs(row, col-1, visited, heights[row][col], heights)    # left
                dfs(row, col+1, visited, heights[row][col], heights)    # right
                dfs(row-1, col, visited, heights[row][col], heights)    # up
                dfs(row+1, col, visited, heights[row][col], heights)    # down

        for i in range(cols):
            dfs(0, i, pac_visited, heights[0][i], heights)
            dfs(rows-1, i, alt_visited, heights[rows-1][i], heights)

        for i in range(rows):
            dfs(i, 0, pac_visited, heights[i][0], heights)
            dfs(i, cols-1, alt_visited, heights[i][cols-1], heights)

        for i in pac_visited:
            if i in alt_visited:
                ans.append(list(i))

        return ans


heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]

s = Solution()
print(s.pacificAtlantic(heights))
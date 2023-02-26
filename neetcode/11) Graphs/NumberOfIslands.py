class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(row, col):
            if row < 0 or row >= len(grid):
                return
            elif col < 0 or col >= len(grid[row]):
                return
            if grid[row][col] == "0":
                return

            grid[row][col] = "0"
            dfs(row-1, col)         # up
            dfs(row+1, col)         # down
            dfs(row, col-1)         # left
            dfs(row, col+1)         # right

        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1":
                    count += 1
                    dfs(row, col)
        return count

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

s = Solution()
print(s.numIslands(grid))
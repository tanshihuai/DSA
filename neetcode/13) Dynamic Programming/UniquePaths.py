class Solution(object):
    '''
    recursive
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 and n == 1:
            return 1
        if m < 1 or n < 1:
            return 0
        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
    '''

    # dp
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        grid = []
        for i in range(m+1):
            row = []
            for j in range(n+1):
                row.append(0)
            grid.append(row)
        grid[1][1] = 1
        for i in range(1,m+1):
            for j in range(1, n+1):
                if i ==1 and j ==1:
                    continue
                grid[i][j] = grid[i-1][j] + grid[i][j-1]

        return grid[m][n]

s = Solution()
print(s.uniquePaths(23,12))
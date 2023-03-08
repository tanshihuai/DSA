class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        rows = len(mat)
        cols = len(mat[0])
        ans = []

        def outOfBounds(row, col):
            if row < 0 or row >= rows:
                return True
            elif col < 0 or col >= cols:
                return True
            return False

        def topright(row, col):
            ans.append(mat[row][col])
            if not outOfBounds(row-1, col + 1):
                return topright(row-1, col+1)
            else:
                if not outOfBounds(row, col+1):
                    return bottomleft(row, col+1)
                elif not outOfBounds(row+1, col):
                    return bottomleft(row+1, col)
                else:
                    return

        def bottomleft(row, col):
            ans.append(mat[row][col])
            if not outOfBounds(row+1, col-1):
                return bottomleft(row+1, col-1)
            else:
                if not outOfBounds(row+1, col):
                    return topright(row+1, col)
                elif not outOfBounds(row, col+1):
                    return topright(row, col+1)
                else:
                    return

        topright(0, 0)
        return ans

mat = [[1,2],[3,4]]
s = Solution()
print(s.findDiagonalOrder(mat))
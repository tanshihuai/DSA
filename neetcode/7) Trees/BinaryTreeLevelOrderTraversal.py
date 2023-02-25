
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

x = TreeNode(3)
x.left = TreeNode(9)
x.right = TreeNode(20)


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans = []
        queue = [[root]]
        while queue:
            current = queue.pop(0)
            tmp = []
            level = []
            for i in current:
                if not i: continue
                if i.left:
                    tmp.append(i.left)
                if i.right:
                    tmp.append(i.right)
                level.append(i.val)
                print(f'{i.val}')
            if tmp: queue.append(tmp)
            ans.append(level)
        return ans




s = Solution()
s.levelOrder(x)
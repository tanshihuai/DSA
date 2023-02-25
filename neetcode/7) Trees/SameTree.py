# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # check for root value
        if not p and not q:
            return True
        else:
            if (p and not q) or (q and not p):
                return False
        if p.val != q.val:
            return False

        left_equals = self.isSameTree(p.left, q.left)
        right_equals = self.isSameTree(p.right, q.right)
        return left_equals and right_equals

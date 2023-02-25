# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        def fullmatch(root, subRoot):
            if not root and not subRoot:
                return True
            elif (not root and subRoot) or (not subRoot and root):
                return False
            if root.val != subRoot.val:
                return False
            else:
                return fullmatch(root.left, subRoot.left) and fullmatch(root.right, subRoot.right)

        if fullmatch(root, subRoot):
            return True
        if not root:
            return False
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def exist(node):
            if inside(node, p.val):
                return inside(node.left, q.val) or inside(node.right, q.val) or inside(node, q.val)
            if inside(node, q):
                return inside(node.left, p.val) or inside(node.right, p.val) or inside(node, p.val)
            return False

        def inside(node, value):
            if not node:
                return False
            if node.val == value:
                return True
            return inside(node.left, value) or inside(node.right, value)


        if not exist(root.left) and not exist(root.right):
            return root
        if exist(root.left):
            return self.lowestCommonAncestor(root.left, p, q)
        elif exist(root.right):
            return self.lowestCommonAncestor(root.right, p, q)

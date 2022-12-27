'''
https://leetcode.com/problems/binary-tree-level-order-traversal/
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def levelOrder(self, root):
        ans = []
        levels = [root]
        while root and levels:
            level_values = []
            next_level = []
            for i in levels:
                level_values.append(i.val)
                if i.left:
                    next_level.append(i.left)
                if i.right:
                    next_level.append(i.right)
            ans.extend([level_values])
            levels = next_level
        return ans
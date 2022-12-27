class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums == []:
            return
        max_index = nums.index(max(nums))
        left = nums[:max_index]
        right = nums[max_index+1:]
        node = TreeNode(max(nums))
        node.left = self.constructMaximumBinaryTree(left)
        node.right = self.constructMaximumBinaryTree(right)
        return node


nums = [3,2,1,6,0,5]
s = Solution()
print(s.constructMaximumBinaryTree(nums))
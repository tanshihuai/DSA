class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return min(nums[0], nums[1])
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        if nums[mid-1] > nums[mid]:
            return nums[mid]
        elif nums[mid] > nums[mid+1]:
            return nums[mid+1]
        elif nums[mid] < nums[-1]:
            return self.findMin(left)
        elif nums[mid] > nums[-1]:
            return self.findMin(right)







nums = [2,3,4,5,1]

s = Solution()
x = s.findMin(nums)
print(x)

'''
pick a value
if value's left is larger than value:
    value is the smallest number in the array
if value's right is smaller than value:
    value's right is smallest number in array

if mid is larger than first element,
    smallest element is on the left
elif mid is larger than the last element,
    smallest element is on the right
'''
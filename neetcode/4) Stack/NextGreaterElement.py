class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        dict1 = {i: -1 for i in nums2}
        ans = []
        for i, e in enumerate(nums2):
            while stack and nums2[stack[-1]] < e:
                index = stack.pop()
                dict1[nums2[index]] = e
            stack.append(i)
        for i in nums1:
            ans.append(dict1[i])
        return ans

nums1 = [1,3,5,2,4]
nums2 = [5,4,3,2,1]
s = Solution()
print(s.nextGreaterElement(nums1, nums2))

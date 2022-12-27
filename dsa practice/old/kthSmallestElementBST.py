class Solution:
    def kthSmallest(self, root, k):
        arr = []
        def lot(root, arr):
            if not root:
                return
            else:
                lot(root.left, arr)
                arr.append(root.val)
                lot(root.right, arr)
        lot(root, arr)
        ans = arr[k-1]
        return ans

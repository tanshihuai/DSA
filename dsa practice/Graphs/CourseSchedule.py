class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        nonreq = set([i for i in range(numCourses)])
        req = set()
        for i in prerequisites:
            nonreq.remove(i[0])
            req.add(i[0])
        print(nonreq)
        print(req)


s = Solution()
pq = [[1,2], [2,3], [3,4]]
print(s.canFinish(5,pq))
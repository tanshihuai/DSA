class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        dict1 = {}
        for i in strs:
            i_sorted = ''.join(sorted(i))
            print(i_sorted)
            if dict1.get(i_sorted):
                dict1[i_sorted].append(i)
            else:
                dict1[i_sorted] = [i]

        ans = []
        for k,v in dict1.items():
            ans.append(v)
        return ans

strs = ["eat","tea","tan","ate","nat","bat"]
s = Solution()
print( s.groupAnagrams(strs) )
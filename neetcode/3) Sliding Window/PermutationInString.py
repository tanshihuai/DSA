class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        '''
        original answer, O(26*n)
        
        
        
        dict1 = {}
        dict2 = {}
        if len(s1) > len(s2):
            return False

        for i in s1:
            dict1[i] = dict1.get(i, 0) + 1

        l = 0
        r = 0
        while r < len(s1):
            dict2[s2[r]] = dict2.get(s2[r], 0) + 1
            r += 1
        if dict1 == dict2:
            return True

        while r < len(s2):
            dict2[s2[r]] = dict2.get(s2[r], 0) + 1
            dict2[s2[l]] = dict2.get(s2[l], 0) - 1
            dict2 = {x:y for x,y in dict2.items() if y is not 0}
            r += 1
            l += 1
            if dict1 == dict2:
                return True
        return False
        '''
        if len(s2) < len(s1):
            return False
        dict1 = {}
        dict2 = {}
        for i in range(97, 123):
            dict1[chr(i)] = 0
            dict2[chr(i)] = 0
        for i in s1:
            dict1[i] = dict1.get(i, 0) + 1

        l = 0
        r = 0
        match = 0
        while r < len(s1):
            dict2[s2[r]] = dict2.get(s2[r], 0) + 1
            r += 1
        for i in range(97, 123):
            if dict1.get(chr(i), 0) == dict2.get(chr(i), 0):
                match += 1
        if match == 26:
            return True

        while r < len(s2):
            dict2[s2[r]] += 1
            if dict2[s2[r]] == dict1[s2[r]]: match += 1
            if dict2[s2[r]] == dict1[s2[r]] + 1: match -= 1     # you just added an "a". If (and only if) the number of "a"s in dict2 is now one more than dict1, it means that it was previously matching but not anymore.
            dict2[s2[l]] -= 1
            if dict2[s2[l]] == dict1[s2[l]]: match += 1
            if dict2[s2[l]] == dict1[s2[l]] - 1: match -= 1     # you just removed an "a". If (and only if) the number of "a"s in dict2 is now one lesser than dict1, it means that it was previously matching but not anymore.
            l += 1
            r += 1
            if match == 26: return True
        return False



s1 = "ab"
s2 = "eidbaooo"
s = Solution()
print(s.checkInclusion(s1, s2))

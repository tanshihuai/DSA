class Solution:
    def groupAnagrams(self, strs):
        dict = {}
        for i in strs:
            group = ''.join(sorted(i))
            if group not in dict:
                dict[group] = [i]
            else:
                dict[group].append(i)

        return dict.values()
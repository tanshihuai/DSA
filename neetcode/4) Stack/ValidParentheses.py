class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """


        stack = []
        for i in s:
            if i == "(":
                stack.append(")")
            elif i == "[":
                stack.append("]")
            elif i == "{":
                stack.append("}")
            else:
                if not stack:
                    return False
                if stack.pop() != i:
                    return False

        return True if not stack else False

s = "((]])"
ss = Solution()
print(ss.isValid(s))
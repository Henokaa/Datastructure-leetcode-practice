class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        found = 0
        temp = 0 
        if len(s) % 2 != 0:
            return False
        dict = {'(' : ')', '[' : ']', '{' : '}'}
        stack = []
        for i in s:
            if i in dict.keys():
                stack.append(i)
            else:
                if stack == []:
                    temp = max(temp, found)
                    return False
                a = stack.pop()
                found = found + 2
                if i != dict[a]:
                    return False
        return stack == []
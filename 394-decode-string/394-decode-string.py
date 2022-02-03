class Solution:
    def decodeString(self, s: str) -> str:
        res, num = '',0
        stack = []
        for c in s:
            if c.isdigit():
                num = num*10 + int(c)
            elif c == '[':
                stack.append(res)
                stack.append(num)
                res = ''
                num = 0
            elif c == ']':
                snum = stack.pop()
                sstr = stack.pop()
                res = sstr + snum*res
            else:
                res += c
        return res
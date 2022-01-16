class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        s2 = []
        str = ""
        counter = 0 
        for i in s:
            stack.append(i)
            if i == ')':
                while stack:
                    if stack[-1] == '(':
                        stack.pop()
                        break  
                    if stack[-1] == ')':
                        stack.pop()
                    else:
                        s2.append(stack.pop())
                s2.reverse()
                while s2:
                    stack.append(s2.pop())

        str = str.join(stack)
        return str
                    
        
        
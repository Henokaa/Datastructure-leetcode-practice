class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        wrong = 0
        index = 0
        if len(needle) == 0:
            return 0
            
        while i < len(haystack): 
            if haystack[i] == needle[0]:
                index = i
                for x in range(1,len(needle)):
                    i += 1
                    if i == len(haystack):
                        return -1
                    if haystack[i] != needle[x]:
                        wrong = 1
                        break
                if wrong == 0:
                    return index
                i = index
                wrong = 0
            i += 1
        return -1
                    
                    
                        
                    
                    
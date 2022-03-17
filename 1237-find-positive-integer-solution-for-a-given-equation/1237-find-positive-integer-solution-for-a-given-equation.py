"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        
        result =[]
        for x in range(1,z+1):
            l,h=1,z
            while(l<=h):
                m=(l+h)//2
                if (customfunction.f(x,m)==z):
                    result.append([x,m])
                    break;
                elif (customfunction.f(x,m)<z):
                    l=m+1
                elif (customfunction.f(x,m)>z):
                    h=m-1
        return result
        
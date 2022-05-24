from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        c = 0
        visitedset = set()
        for i in range(len(prerequisites)):
            preMap[prerequisites[i][c]].append(prerequisites[i][c+1])
        
        def dfs(cru):
            if cru in visitedset:
                return False
            visitedset.add(cru)
            if cru in preMap:
                for j in preMap[cru]:
                    if dfs(j) == False:
                        return False
                visitedset.remove(cru)
                preMap[cru] = [] # without this we will have time complexity 
            else:
                visitedset.remove(cru)
                preMap[cru] = []
                return True        
        
        for i in range(numCourses):
            if dfs(i) == False:
                return False
        return True
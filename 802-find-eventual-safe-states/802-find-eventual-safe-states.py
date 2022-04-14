class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = {}
        def dfs(i): # dfs(0)
            if i in safe:
                return safe[i]
            safe[i] = False
            for nei in graph[i]: # all the children of 0
                if not dfs(nei): # if the children is not safe then it is not safe, if thereiscycle
                    return False
            safe[i] = True # if it does it create cycle its true
            return True
            
        res = []
        for i in range(n):
            if dfs(i):
                res.append(i)
        return res
        
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        provinces = 0
        
        def dfs(i, isConnected):
            visited.add(i)
        
            for j in range(len(isConnected[0])):
                if j not in visited and isConnected[i][j] != 0:
                    dfs(j, isConnected)
        
        for i in range(len(isConnected)):
            if i not in visited:
                provinces += 1
            dfs(i, isConnected)
            
        return provinces
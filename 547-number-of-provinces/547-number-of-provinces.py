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
    
    '''
      1 2 3
    1|1 1 0
    2|1 1 0
    3|0 0 1
    
    it passes the first row to the dfs then visit every thing in that row, go to the second row
    same their then on the third because it is not in visited it increase by one.
    '''
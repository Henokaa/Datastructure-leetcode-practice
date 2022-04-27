class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parent = [i for i in range(len(isConnected))]
        rank = [1] * len(isConnected) # rank no children not depth
        count = len(isConnected)
        
        def findset(x):
            if x == parent[x]:
                return x
            parent[x] = findset(parent[x])
            return parent[x]
        def union(x,y):
            x = findset(x)
            y = findset(y)
            if x != y:
                
                if rank[x] >= rank[y]:
                    parent[y] = x
                    rank[x] += rank[y]
                else:
                    parent[x] = y
                    rank[y] += rank[x]
                nonlocal count    
                count -= 1
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if i!=j and isConnected[i][j] == 1:
                    union(i,j)
        return count
                    
                
                
                
            
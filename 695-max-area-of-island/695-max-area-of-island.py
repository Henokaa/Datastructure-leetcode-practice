class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        parent = defaultdict()
        rank = defaultdict()
        direction = [[1,0],[0,1],[-1,0],[0,-1]]
        in_bound = lambda r, c : 0 <= r < len(grid) and 0 <= c < len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    parent[(i,j)] = (i,j)
                    rank[(i,j)] = 1
                
        def findset(x):
            if x == parent[x]:
                return x
            
            parent[x] = findset(parent[x])
            return parent[x]
        
        def unionset(x,y):
            x = findset(x)
            y = findset(y)
            
            if x != y:
                if rank[x] > rank[y]:
                    parent[y] = x
                elif rank[x] < rank[y]:
                    parent[x] = y
                else:
                    parent[x] = y
                    rank[x] += 1
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    for r,c in direction:
                        ni, nj = i + r, j + c
                        if in_bound(ni, nj) and grid[ni][nj] == 1 :
                            unionset((i,j), (ni,nj))

        count = defaultdict()
        maxcount = 0
        for k in parent.keys():
            v = findset(parent[k])
            if v in count:
                count[v] += 1
            else:
                count[v] = 1
            maxcount = max(maxcount, count[v])

        return maxcount
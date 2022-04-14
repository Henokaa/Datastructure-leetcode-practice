class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """
        1. find all nodes that do not have outgoing edges -> terminal node
        2. reverse all edges
        3. from each terminal node, do BFS/DFS, the node we are reaching at the end are safe nodes
        """
        q = deque()
        visited = set()
        
        
        # counts how many times a node is left to reach
        cnt = Counter()
        
        n_table = defaultdict(list)
        for i, neighbors in enumerate(graph):
            # count how many outgoing edges, -1 when reached
            cnt[i] = len(neighbors)
            # record reverse edge
            for n in neighbors: # saving the parents for each node just like indegree
                n_table[n].append(i)
            if len(neighbors) == 0:
                # no outgoing edges, set as start
                q.append(i) # elements with no child
                visited.add(i) 
        print(cnt)
        '''
        graph - ({0: 2, 1: 2, 2: 1, 3: 1, 4: 1, 5: 0, 6: 0}) 0 have two child
        parent -  {1: [0], 2: [0, 1], 3: [1], 5: [2, 4], 0: [3]} decrease 1 in the number of                                                                        child in parent. 
        '''
        res = []
        
        while q:
            curr = q.popleft()
            
            res.append(curr) 
            
            for neighbor in n_table[curr]: # 
                cnt[neighbor] -= 1
                if neighbor not in visited and cnt[neighbor] == 0:
                    q.append(neighbor)
                    visited.add(neighbor)
                    
        return sorted(res)
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        from collections import defaultdict
        visited_accounts = [False] * len(accounts)
        emails_accounts_map = defaultdict(list)
        res = []
        # Build up the graph.
        
        for i in range(len(accounts)):
            for j in range(len(accounts[i])):
                email = accounts[i][j]
                emails_accounts_map[email].append(i)
        print(emails_accounts_map)
        
        def dfs(emails, i):
            if visited_accounts[i]:
                return
            visited_accounts[i] = True
            
            for x in range(len(accounts[i])):
                if x == 0:
                    continue
                emails.add(accounts[i][x])
                for a in emails_accounts_map[accounts[i][x]]:
                    dfs(emails, a)
            

        for i, account in enumerate(accounts):
            if visited_accounts[i]:
                continue
            emails = set()
            name = accounts[i][0]
            dfs(emails, i)
            res.append([name] + sorted(emails))
        return res
            
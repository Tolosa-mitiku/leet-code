class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]: 
        parent = {}
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                parent[accounts[i][j]] = accounts[i][j]
                
        
        def find(a):
            if parent[a] != a:
                parent[a] = find(parent[a])
            return parent[a]
        def union(u, v):
            parent[find(u)] = find(v)
        
        
        for i in range(len(accounts)):
            for j in range(2, len(accounts[i])):
                union(accounts[i][j-1], accounts[i][j])
        
        
        groupedemail = defaultdict(list)
        visited = set()
        
        res = []
        for email in parent:
            groupedemail[find(email)].append(email)
        
        for i in range(len(accounts)):
            parentt = find(accounts[i][1])
            if parentt not in visited:
                groupedemail[parentt].sort()
                res.append([accounts[i][0]] + groupedemail[parentt])
                visited.add(parentt)
        return res
                
        
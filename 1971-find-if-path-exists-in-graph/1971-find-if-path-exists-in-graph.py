class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent = [i for i in range(n)]
        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]
        def union(u, v):
            parent[find(u)] = find(v)
        
        for i, j in edges:
            union(i, j)
        
        return find(source) == find(destination)
        
        
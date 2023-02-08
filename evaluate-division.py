class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = defaultdict(set)
        for i in range(len(values)):
            x, y = equations[i]
            graph[x].add((y, values[i]))
            graph[y].add((x, 1.0 / values[i]))


        def dfs(graph, start, end, visited):
            if start == end and graph[start]:
                return 1.0
            
            visited.add(start)
            for neigh, val in graph[start]:
                if neigh in visited:
                    continue
                
                tmp = dfs(graph, neigh, end, visited)
                if tmp > 0:
                    return val * tmp
            
            return -1.0
            
        
        res = []
        for query in queries:
            res.append(dfs(graph, query[0], query[1], set()))
        
        return res
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = defaultdict(list)
        
        for i, j in roads:
            graph[i].append(j)
            graph[j].append(i)
        
        def dfs(node):
            if node != 0 and len(graph[node]) == 1:
                return 1, 1
            fuel = 0
            passenger = 0
            for i in graph[node]:
                if i not in visited:
                    visited.add(i)
                    i, j = dfs(i)
                    fuel += i
                    passenger += j
            passenger += 1
            if node == 0:
                return fuel, passenger
            return fuel + ceil(passenger / seats), passenger
        visited = set([0])
        return dfs(0)[0]
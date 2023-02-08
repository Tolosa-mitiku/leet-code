class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        stops = defaultdict(set)

        for i in range(len(routes)):
            for j in range(len(routes[i])):
                stops[routes[i][j]].add(i)

        queue = deque([(i, 1) for i in stops[source]])
        visited = set([i for i in stops[source]])
        while queue:
            bus, num = queue.popleft()
            for j in range(len(routes[bus])):
                if routes[bus][j] == target:
                    return num
                for buses in stops[routes[bus][j]]:
                    if buses not in visited:
                        visited.add(buses)
                        queue.append((buses, num + 1))
        return -1


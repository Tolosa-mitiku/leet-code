class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque([0])
        visited = set()
        while queue:
            curr = queue.popleft()
            visited.add(curr)
            for i in rooms[curr]:
                if i not in visited:
                    queue.append(i)
        return visited == set(range(len(rooms)))
                
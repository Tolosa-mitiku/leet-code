class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        queue = deque([[0, [0]]])
        ans = []
        while queue:
            curr = queue.popleft()
            for i in graph[curr[0]]:
                temp = curr[1][:]
                print(temp)
                temp.append(i)
                queue.append([i, temp])
                if i == len(graph)-1:
                    ans.append(temp)
        return ans
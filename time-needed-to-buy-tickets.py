class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque([(i, tickets[i]) for i in range(len(tickets))])
        ans = 0
        while queue:
            ind, curr = queue.popleft()
            if curr - 1 != 0:
                queue.append((ind, curr - 1))
            elif ind == k:
                return ans + 1
            ans += 1
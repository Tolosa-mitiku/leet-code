class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        ans = float("inf")

        left, right = 0, 0
        limit = 0
        while right < len(blocks):
            if right < k:
                if blocks[right] == "W":
                     limit += 1
                right += 1
            else:
                ans = min(ans, limit)
                limit += blocks[right] == "W"
                limit -= blocks[left] == "W"
                right += 1
                left += 1

        return min(ans, limit)
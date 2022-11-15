class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counterP = Counter(p)
        
        counter = defaultdict(int)
        left, right = 0, 0
        ans = []
        while right < len(s):
            counter[s[right]] += 1
            if right - left == len(p)-1:
                if counter == counterP:
                    ans.append(left)
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
            right += 1
        return ans
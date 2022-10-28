class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for word in strs:
            temp = list(word)
            temp.sort()
            ans["".join(temp)].append(word)
        return ans.values()
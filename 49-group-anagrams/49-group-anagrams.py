class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for string in strs:
            sortedstr = list(string)
            sortedstr.sort()
            ans["".join(sortedstr)].append(string)
        return ans.values()
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        string = list(s)
        string.sort(key=lambda x: (counter[x], x), reverse= True)
        return "".join(string)
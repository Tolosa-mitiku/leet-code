class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        counter1 = Counter(word1)
        values1 = list(counter1.values())
        values1.sort()
        counter2 = Counter(word2)
        values2 = list(counter2.values())
        values2.sort()
        return values1 == values2 and set(counter1.keys()) == set(counter2.keys())
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        counter = defaultdict(int)
        total = set()
        for w, l in matches:
            counter[l] += 1
            total.add(w)
            total.add(l)
        undefeated = list(total.difference(set(counter.keys())))
        undefeated.sort()
        
        onetimeloser = [i for i in counter.keys() if counter[i] == 1]
        onetimeloser.sort()
        
        return [undefeated, onetimeloser]
        
        
        
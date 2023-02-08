class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        dict1 = defaultdict(set)
        dict2 = defaultdict(set)
        sett = set()
        ans = []
        counter = defaultdict(int)
        for x, y in adjacentPairs:
            counter[x] += 1
            counter[y] += 1
            dict1[x].add(y)
            dict2[y].add(x)

        first = 0
        for i in counter:
            if counter[i] == 1:
                first = i
                ans.append(first)
                sett.add(first)
                break
            

        for _ in range(len(adjacentPairs)):
            if first in dict1:
                for el in dict1[first]:
                    if el not in sett:
                        first = el
                        ans.append(first)
                        sett.add(first)
            if first in dict2:
                for el in dict2[first]:
                    if el not in sett:
                        first = el
                        ans.append(first)
                        sett.add(first)

        return ans


        
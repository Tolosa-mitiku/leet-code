class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 == 1:
            return []

        list1 = defaultdict(int)
        for i in changed:
            list1[i] += 1
        
        zerocase = False
        for i in sorted(list1):
            if i == 0 and not zerocase:
                if list1[i] % 2== 0:
                    list1[0] = list1[0] // 2
                else:
                    return []
                zerocase = True
            elif i != 0 and list1[i] > 0 and i*2 in list1 and list1[i * 2] > 0:
                list1[i * 2] -= min(list1[i], list1[i*2])
            
        list2 = []
        
        for i in list1:
            for j in range(list1[i]):
                list2.append(i)
        
        if len(list2) != len(changed)//2:
            return []
        return list2
            
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        pathfile = defaultdict(list)
        for i in range(len(paths)):
            temp = paths[i].split(" ")
            for i in range(1, len(temp)):
                temp2 = temp[i].split("(")
                pathfile[temp2[1]].append(temp[0]+ "/" + temp2[0])
        ans = []
        for i in pathfile.values():
            if len(i) > 1:
                ans.append(i)
        return ans
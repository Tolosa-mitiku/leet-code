class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        
        count = len(words[0])
        temp = [words[0]]
        for i in range(1, len(words)):
            count += len(words[i])+1
            if count > maxWidth:
                ans.append(temp)
                temp = []
                count = len(words[i])
            temp.append(words[i])
        ans.append(temp)
        res = []
        for i in range(len(ans)-1):
            if len((ans[i])) == 1:
                dsf = "".join(ans[i][0])
                res.append(dsf  + " " * (maxWidth - len(ans[i][0])))
                continue
            count = 0
            for j in range(len(ans[i])):
                count += len(ans[i][j])
            total = maxWidth - count
            length = len(ans[i])-1
            module = total % length
            spaces = total // length
            
            temp = []
            for j in range(len(ans[i])-1):
                temp.append(ans[i][j])
                temp.append(" "*spaces)
                if module > 0:
                    temp.append(" ")
                    module -= 1
            temp.append(ans[i][-1])
            res.append("".join(temp))
        dsf = " ".join(ans[-1])
        res.append(dsf  + " " * (maxWidth - sum(len(i) for i in ans[-1]) - len(ans[-1]) + 1))
        return res
            
                
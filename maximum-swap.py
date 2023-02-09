class Solution:
    def maximumSwap(self, num: int) -> int:

        ans = num

        temp = list(str(num))
        for i in range(len(temp)):
            for j in range(i, len(temp)):
                temp2 = list(temp)
                temp2[i], temp2[j] = temp2[j], temp2[i]
                if int("".join(temp2)) > ans:
                    ans = eval("".join(temp2))
        return ans
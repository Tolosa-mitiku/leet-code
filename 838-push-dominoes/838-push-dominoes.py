class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list(dominoes)
        left = 0
        isfirst = True
        for i in range(len(dominoes)):
            if dominoes[i] == "." and isfirst:
                left = i
                isfirst = False
            if dominoes[i] != "." and not isfirst:
                if left == 0:
                    if dominoes[i] == "L":
                        temp = dominoes[i]
                        for i in range(left, i+1):
                            dominoes[i] = temp
                elif dominoes[left-1] == dominoes[i]:
                    temp = dominoes[i]
                    for i in range(left, i+1):
                        dominoes[i] = temp
                else:
                    if dominoes[left-1] == "R":
                        leftval = dominoes[left-1]
                        rightval = dominoes[i]
                        templeft = left
                        tempright = i-1
                        while templeft < tempright:
                            dominoes[templeft] = leftval
                            dominoes[tempright] = rightval
                            templeft += 1
                            tempright -= 1
                isfirst = True
        if not isfirst:
            if dominoes[left-1] == "R":
                for i in range(left, len(dominoes)):
                    dominoes[i] = dominoes[left-1]
        return "".join(dominoes)
                
class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = 0
        curr = chars[0]
        temp = 1
        for i in range(1, len(chars)):
            if chars[i] != curr:
                chars[ans] = curr
                ans += 1
                if temp > 1:
                    tempstr = str(temp)
                    for j in tempstr:
                        chars[ans] = j
                        ans += 1
                curr = chars[i]
                temp = 1
            else:
                temp += 1
        chars[ans] = curr
        ans += 1
        if temp > 1:
            tempstr = str(temp)
            for j in tempstr:
                chars[ans] = j
                ans += 1
        return ans
                
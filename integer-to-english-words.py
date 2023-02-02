class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        kilo = ["Billion", "Million", "Thousand"]
        ones = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        tens = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        num = str(num)
        nums = []

        for i in range(len(num)-1,-1,-3):
            temp = []
            for j in range(min(3, i+1)):
                temp.append(num[i - j])
            temp.reverse()
            nums.append(temp)
        nums.reverse()

        ans = []

        for i in range(len(nums)):
            tempans = []
            if len(nums[i]) == 3:
                if eval(nums[i][0]) != 0:
                    tempans.append(ones[eval(nums[i][0])-1])
                    tempans.append("Hundred")
                if eval(nums[i][1]) != 0:
                    if eval("".join(nums[i][1:])) - 1 < len(ones):
                        tempans.append(ones[eval("".join(nums[i][1:])) - 1])
                    else:
                        tempans.append(tens[eval(nums[i][1])-2])
                        if eval(nums[i][2]) != 0:
                            tempans.append(ones[eval(nums[i][2])-1])
                else:
                    if eval(nums[i][2]) != 0:
                        tempans.append(ones[eval(nums[i][2])-1])
            elif len(nums[i]) == 2:
                if eval("".join(nums[i])) - 1 < len(ones):
                    tempans.append(ones[eval("".join(nums[i])) - 1])
                else:
                    tempans.append(tens[eval(nums[i][0])-2])
                    if eval(nums[i][1]) != 0:
                        tempans.append(ones[eval(nums[i][1])-1])
            else:
                if eval(nums[i][0]) != 0:
                    tempans.append(ones[eval(nums[i][0])-1])
            if tempans:
                if 4-len(nums)+i < 3:
                    tempans.append(kilo[4-len(nums)+i])
                ans.append(" ".join(tempans))

        return " ".join(ans)
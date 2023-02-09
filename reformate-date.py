class Solution:
    def reformatDate(self, date: str) -> str:
        ans = []
        months = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
        date2 = date.split()


        year = date2[2]

        ans.append(year)

        month = str(months[date2[1]])
        if len(month) == 1:
            month = "0" + month
        ans.append(month)

        day = ""
        for i in date2[0]:
            if i.isdigit():
                day += i
        if len(day) == 1:
            day = "0" + day
        ans.append(day)

        return "-".join(ans)
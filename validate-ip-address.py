class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if '.' in queryIP:
            x = queryIP.split('.')
            if len(x) != 4 or '' in x:
                return "Neither"
            for num in x:
                if len(num)>1:
                    if num[0]=='0':
                        return "Neither"
                for c in num:
                    if not c.isdigit():
                        return "Neither"
                if int(num) < 0 or int(num) > 255:
                    return "Neither"
            return "IPv4"
        
        if ':' in queryIP:
            h = queryIP.split(':')
            if len(h) != 8 or '' in h:
                return "Neither"
            for str in h:
                for c in str:
                    if not (c.isdigit() or c in "abcdefABCDEF"):
                        return "Neither"
                if len(str)<1 or len(str)>4:
                    return "Neither"
            return "IPv6"
                
        return "Neither"
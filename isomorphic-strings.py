class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}
        
        for i in range(len(s)):
            if not dict1.get(s[i]):
                dict1[s[i]] = t[i]
            elif dict1[s[i]] == t[i]:
                continue
            else:
                return False
            
        for i in range(len(s)):
            if not dict2.get(t[i]):
                dict2[t[i]] = s[i]
            elif dict2[t[i]] == s[i]:
                continue
            else:
                return False
        return True
    
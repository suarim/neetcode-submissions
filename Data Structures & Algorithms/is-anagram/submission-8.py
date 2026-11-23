class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h ={}
        if len(s) != len(t):
            return False
        for i in s:
            if i in h:
                h[i]= h[i]+1
            else:
                h[i]=1
        for i in t:
            if i in h:
                h[i]= h[i]-1
                if h[i]<0:
                    return False
            else:
                return False
        return True
    
class Solution:
    def isAnagram(self, s: str, k: str) -> bool:
        h={}
        t={}
        for i in s:
            if i in h:
                h[i]+=1
            else:
                h[i]=1
        for i in k:
            if i in t:
                t[i]+=1
            else:
                t[i]=1
        return h==t
        
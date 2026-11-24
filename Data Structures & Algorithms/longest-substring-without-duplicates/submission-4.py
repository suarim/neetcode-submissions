class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        res=set()
        maxa=0
        for r in range(len(s)):
            while s[r] in  res:
                res.remove(s[i])
                i+=1
            res.add(s[r])
            maxa=max(maxa,r-i+1)
        return maxa
        
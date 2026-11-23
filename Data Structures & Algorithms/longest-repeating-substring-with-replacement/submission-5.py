from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        h={}
        l=0
        res=0
        max_freq=0
        for  r in range(len(s)):
            h[s[r]] = h.get(s[r], 0) + 1
            max_freq = max(max_freq, h[s[r]])

            while r-l+1 - max_freq>k:
                h[s[l]]-=1
                if h[s[l]]==0:
                    del h[s[l]]
                l+=1
            res=max(res,r-l+1)
        return res

        
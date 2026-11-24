class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        maxa=0
        h={0:0}
        for r in range(len(s)):
            if s[r] in h:
                h[s[r]]+=1
            else:
                h[s[r]]=1
            while (r-l+1)-max(h.values()) > k:
                h[s[l]]-=1
                l+=1
            
            maxa=max(r-l+1,maxa)
        return maxa
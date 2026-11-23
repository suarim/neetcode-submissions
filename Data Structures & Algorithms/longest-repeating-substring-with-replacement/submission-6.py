class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        maxa=0
        h={}
        for r in range(len(s)):
            h[s[r]]=h.get(s[r],0)+1
            while (r-l+1)-max(h.values())>k:
                h[s[l]]-=1
                l+=1
            maxa=max(maxa,r-l+1)
        return maxa


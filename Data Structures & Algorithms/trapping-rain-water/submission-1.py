class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        maxl=0
        hl=[0]*len(height)
        hr=[0]*len(height)
        maxr=0
        for i in range(len(height)):
            maxl=max(maxl,height[i])
            hl[i]=maxl
        for i in range(len(height)-1,-1,-1):
            maxr=max(maxr,height[i])
            hr[i]=maxr
        tp=0
        for i in range(len(height)):
            tp+=min(hl[i],hr[i])-height[i]
        return tp
class Solution:
    def maxArea(self, h: List[int]) -> int:
        l=0
        r=len(h)-1
        maxa=-111111111
        while l<r:
            area=min(h[l],h[r])*(r-l)
            if h[l]<=h[r]:
                l+=1
            else:
                r-=1
            maxa=max(area,maxa)
        return maxa
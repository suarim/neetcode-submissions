class Solution:
    def trap(self, h: List[int]) -> int:
        l,r,w=0,len(h)-1,0
        lmax,rmax=h[l],h[r]
        while l<r:
            if lmax<rmax:
                l+=1
                lmax=max(lmax,h[l])
                w+=lmax-h[l]
            else:
                r-=1
                rmax=max(rmax,h[r])
                w+=rmax-h[r]
        return w
               
        
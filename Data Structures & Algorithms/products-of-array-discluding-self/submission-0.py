class Solution:
    def productExceptSelf(self, l: List[int]) -> List[int]:
        presum=[1]
        postsum=[1]
        for i in range(len(l)):
            presum.append(presum[-1]*l[i])
        for i in range(len(l)-1,-1,-1):
            postsum.insert(0,l[i]*postsum[0])
        res=[]
        for i in range(len(l)):
            res.append(presum[i]*postsum[i+1])
        return res
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ansl=[1]*n
        ansr=[1]*n
        res=[1]*n
        for i in range(1,n):
            ansl[i]=ansl[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            ansr[i]=ansr[i+1]*nums[i+1]
        for i in range(n):
            res[i]=ansl[i]*ansr[i]
        return res

 


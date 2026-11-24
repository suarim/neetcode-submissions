class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ansl=[1]*len(nums)
        ansr=[1]*len(nums)
        res=[1]*len(nums)
        n=len(nums)
        for i in range(1,len(nums)):
            ansl[i]=ansl[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            ansr[i]=ansr[i+1]*nums[i+1]
        for i in range(len(nums)):
            res[i]=ansl[i]*ansr[i]
        return res
            
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxl=0
        numset=set(nums)
        for i,s in enumerate(nums):
            l=0
            if s-1 not in numset:
                while s+l in numset:
                    l+=1
            maxl=max(maxl,l)
        return maxl


        
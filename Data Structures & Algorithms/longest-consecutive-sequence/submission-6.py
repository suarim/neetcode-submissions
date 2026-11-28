class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxl=0
        numset=set(nums)
        for i in nums:
            l=0
            if i-1 not in numset:
                while i+l in numset:
                    l+=1
                maxl=max(l,maxl)
        return maxl
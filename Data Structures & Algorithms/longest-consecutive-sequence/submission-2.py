class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        maxc=1
        c=1
        cur=0
        if len(nums)==0:
            return 0
        for i in numset:
            if i-1 not in numset:
                c=1
                cur=i
            while cur+1 in numset:
                c+=1
                cur+=1
                maxc=max(maxc,c)
        return maxc
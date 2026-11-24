class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={}
        for i,s in enumerate(nums):
            if target-s in h:
                return [h[target-s],i]
            h[s]=i
        return [0,1]
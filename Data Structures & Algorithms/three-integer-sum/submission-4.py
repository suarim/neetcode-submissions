class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=set()
        # [-4,-1,-1,0,1,2]
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while l<r:
                if nums[l]+nums[r]+nums[i] < 0:
                    l+=1
                elif nums[l]+nums[r]+nums[i] > 0:
                    r-=1
                else:
                    res.add(tuple(sorted([nums[l],nums[r],nums[i]])))
                    l+=1
                    r-=1
        return list(res)
                

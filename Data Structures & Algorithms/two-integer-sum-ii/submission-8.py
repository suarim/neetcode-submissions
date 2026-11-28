class Solution:
    def twoSum(self, n: List[int], target: int) -> List[int]:
        l=0
        r=len(n)-1
        while l<r:
            if n[l]+n[r]==target:
                return [l+1,r+1]
            elif n[l]+n[r]<target:
                l+=1
            else:
                r-=1
        return [0,1]
            
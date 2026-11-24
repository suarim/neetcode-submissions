class Solution:
    def twoSum(self, numbers: List[int], t: int) -> List[int]:
        l=0
        r=len(numbers)-1
        while l<r:
            if numbers[l]+numbers[r]<t:
                l+=1
            elif numbers[l]+numbers[r]>t:
                r-=1
            else:
                return [l+1,r+1]
        return [0,0]
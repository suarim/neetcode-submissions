class Solution:
    def twoSum(self, l: List[int], target: int) -> List[int]:
        h={}
        for i,n in enumerate(l):
            h[n]=i
        for i in range(len(l)):
            comp=target-l[i]
            if comp in h and h[comp]!=i:
                return [i,h[comp]]

        
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums)
        num=[[] for i in range(len(nums)+1)]
        # print(c)
        for i,j in c.items():
            num[j].append(i)
        # print(num)
        res=[]
        for i in range(len(num)-1,-1,-1):
            if len(res)!=k:
                res.extend(num[i])
            else:
                return res

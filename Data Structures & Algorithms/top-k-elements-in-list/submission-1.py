from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = Counter(nums)
        buckets = {}
        for i in range(len(nums)+1):
            buckets[i]=[]
        for i,j in h.items():
                buckets[j].append(i)
        res=[]
        for i in range(len(nums),-1,-1):
            if len(buckets[i])!=0:
                res.extend(buckets[i])
            if len(res)==k:
                return res


        
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c= Counter(nums)
        h=[]
        # print(c)
        for i,j in c.items():
            if len(h)<k:
                heapq.heappush(h,(j,i))
            elif len(h)==k:
                heapq.heappushpop(h,(j,i))
            # print(h)
        return [s[1] for s in h]

        
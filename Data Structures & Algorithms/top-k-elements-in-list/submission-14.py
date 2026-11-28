from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h=[]
        count=Counter(nums)

        for i,j in Counter(nums).items():
            if len(h)<k:
                heapq.heappush(h,(j,i))
            else:
                heapq.heappushpop(h,(j,i))

        return [i[1] for i in h]


            
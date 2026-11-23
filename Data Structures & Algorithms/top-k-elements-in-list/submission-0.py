class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h={}
        for i in nums:
            if i in h:
                h[i]+=1
            else:
                h[i]=1
        return sorted(h, key=lambda x:h[x],reverse=True)[:k]
        
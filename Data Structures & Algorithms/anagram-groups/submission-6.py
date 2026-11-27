from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=[]
        h={}
        for i in strs:
            key = tuple(sorted(Counter(i).items()))
            if key not in h:
                h[key]=[]
            h[key].append(i)
        return list(h.values())
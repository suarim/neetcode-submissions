from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h=defaultdict(list)

        for i in strs:
            h[str(sorted(i))].append(i)
        return list(h.values())
        
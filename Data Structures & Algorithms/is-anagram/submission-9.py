from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l = Counter(s)
        r = Counter(t)
        return l==r        
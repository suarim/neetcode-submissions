from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        p=Counter(s)
        q=Counter(t)
        return p==q

        
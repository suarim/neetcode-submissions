from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1count=Counter(s1)
        i=0
        while i<len(s2): #8
            start=i
            end=start+len(s1) # 3
            s2count=Counter(s2[start:end])
            if s1count==s2count:
                return True
            i+=1
        return False
        
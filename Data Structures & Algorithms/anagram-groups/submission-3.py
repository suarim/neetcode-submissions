class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h={}
        for i in strs:
            ch = [0]*26
            for c in i:
                ch[ord(c)-ord('a')]+=1
            count = tuple(ch)
            if count not in h:
                h[count] = []
            h[count].append(i)
        return list(h.values())
        
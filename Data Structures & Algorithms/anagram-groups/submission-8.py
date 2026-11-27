class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h={}
        for i in strs:
            ch=[0]*26
            for s in i:
                ch[ord(s)-ord('a')]+=1
            key = tuple(ch)
            if key not in h:
                h[key]=[]
            h[key].append(i)
        return list(h.values())
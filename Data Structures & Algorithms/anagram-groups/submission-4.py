class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h={}
        for i in strs:
            ch=[0]*26
            for s in i:
                ch[ord(s)-ord('a')]+=1
            ch=tuple(ch)
            if ch not in h:
                h[ch]=[i]
            else:
                h[ch].append(i)
        return list(h.values())
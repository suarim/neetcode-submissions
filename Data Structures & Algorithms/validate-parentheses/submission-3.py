class Solution:
    def isValid(self, s: str) -> bool:
        res=[]
        if len(s)%2!=0:
            return False
        for i in s:
            if i in "({[":
                res.append(i)
            elif i == ")":
                if len(res)!=0 and res[-1]=="(":
                    res.pop()
                else:
                    return False
            elif   i == "]":
                if len(res)!=0 and res[-1]=="[":
                    res.pop()
                else:
                    return False
            elif  i == "}":
                if len(res)!=0 and res[-1]=="{":
                    res.pop()
                else:
                    return False
        return len(res)==0
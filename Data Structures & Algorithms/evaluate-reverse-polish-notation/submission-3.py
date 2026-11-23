class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        l=[]

        for i in tokens:
            if i not in ["+","-","*","/"]:
                l.append(i)
            else:
                b=int(l.pop())
                a=int(l.pop())
                if i=="+":
                    s=a+b
                elif i=="-":
                    s=a-b
                elif i=="*":
                    s=a*b
                else:
                    s=a/b
                l.append(s)
        return int(l[0])

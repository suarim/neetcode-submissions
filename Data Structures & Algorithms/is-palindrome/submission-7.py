class Solution:
    def isPalindrome(self, s: str) -> bool:
        t=[i.lower() for i in s if i not in ["?"," ",",","'",".",":","!"]]
        return t==t[::-1]
        
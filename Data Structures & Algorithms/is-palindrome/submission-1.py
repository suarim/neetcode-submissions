class Solution:
    def isPalindrome(self, s: str) -> bool:
        str="".join(c.lower() for c in s if c.isalnum())

        print(str)
        if str.lower()==str[::-1]:
            return True
        else:
            return False 
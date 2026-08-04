class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        num=0
        n=x
        while x>0:
            ld=x%10
            num=num*10+ld
            x=x//10
        if n==num:
            return True
        return False
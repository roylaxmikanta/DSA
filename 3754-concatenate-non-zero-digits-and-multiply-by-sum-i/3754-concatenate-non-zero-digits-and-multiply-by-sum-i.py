class Solution:
    def sumAndMultiply(self, n: int) -> int:
        num=""
        sumi=0
        while n>0:
            ld=n%10
            if ld!=0:
                num=num+str(ld)
                sumi+=ld
            n=n//10
        if num=="":
            return 0
        return sumi*int(num[::-1])
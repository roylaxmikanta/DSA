class Solution:
    def convertToBase7(self, num: int) -> str:
        if num==0:
            return "0"
        nega=num<0
        num=abs(num)
        res=[]
        while num>0:
            remainder=num%7
            res.append(str(remainder))
            num//=7
        if nega:
            res.append("-")
        return "".join(reversed(res))
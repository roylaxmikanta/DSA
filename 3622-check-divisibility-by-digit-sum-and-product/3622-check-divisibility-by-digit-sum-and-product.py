class Solution:
    def checkDivisibility(self, n: int) -> bool:
        temp=n
        sumi=0
        prod=1
        while temp>0:
            ld=temp%10
            sumi+=ld
            prod*=ld
            temp//=10
        return n%(sumi+prod)==0
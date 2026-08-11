class Solution:
    def Iszero(self,n):
        while n>0:
            if n%10==0:
                return False
            n//=10
        return True
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1,(n//2)+1):
            if self.Iszero(i) and self.Iszero(n-i):
                return [i,n-i]
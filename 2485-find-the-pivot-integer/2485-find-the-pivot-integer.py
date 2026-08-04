class Solution:
    def pivotInteger(self, n: int) -> int:
        if n==1:
            return 1
        total=n*(n+1)/2
        sumi=0
        for i in range(1,n+1):
            sumi+=i
            if sumi==total-sumi+i:
                return i
        return -1
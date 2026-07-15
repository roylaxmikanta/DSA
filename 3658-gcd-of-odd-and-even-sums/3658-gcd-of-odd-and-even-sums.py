from math import gcd
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        i=1
        sumOdd=0
        sumEven=0
        while i<=n:
            sumOdd+=2*i-1
            sumEven+=2*i
            i+=1
        return gcd(sumOdd,sumEven)
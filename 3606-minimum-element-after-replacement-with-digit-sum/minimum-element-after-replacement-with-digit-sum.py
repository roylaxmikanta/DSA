class Solution:
    def minElement(self, nums: List[int]) -> int:
        def sumiOfDigits(n):
            sumi=0
            while n>0:
                ld=n%10
                sumi+=ld
                n=n//10
            return sumi
        mini=float("inf")
        for n in nums:
            mini=min(mini,sumiOfDigits(n))
        return mini

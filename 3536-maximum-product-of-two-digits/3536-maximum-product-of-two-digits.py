class Solution:
    def maxProduct(self, n: int) -> int:
        ans=[]
        while n>0:
            ans.append(n%10)
            n//=10
        ans.sort()
        return ans[-1]*ans[-2]
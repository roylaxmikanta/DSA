class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        prev2=1
        prev=2
        for i in range(3,n+1):
            curr=prev+prev2
            prev2=prev
            prev=curr
        return prev
        
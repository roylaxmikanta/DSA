class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        # dp=[[None]*n for _ in range(n)]
        prev=[-1]*n
        for j in range(n):
            prev[j]=triangle[n-1][j]
        for i in range(n-2,-1,-1):
            curr=[-1]*n
            for j in range(0,i+1):
                down=triangle[i][j]+prev[j]
                corner=triangle[i][j]+prev[j+1]
                curr[j]=min(down,corner)
            prev=curr
        return prev[0]
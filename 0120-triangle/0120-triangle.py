class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        dp=[[None]*n for _ in range(n)]
        def func(i,j):
            if i==len(triangle)-1:
                return triangle[i][j]
            if dp[i][j]!=None:
                return dp[i][j]
            down=triangle[i][j]+func(i+1,j)
            corner=triangle[i][j]+func(i+1,j+1)
            dp[i][j]=min(down,corner)
            return dp[i][j]
        return func(0,0)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp=[[-1]*n for _ in range(m)]
        dp[0][0]=grid[0][0]
        def solve(i,j):
            if i==0 and j==0:
                return dp[0][0]
            if i<0 or j<0:
                return float('inf')
            if dp[i][j]!=-1:
                return dp[i][j]
            up=solve(i-1,j)
            left=solve(i,j-1)
            dp[i][j]=grid[i][j]+min(up,left)
            return dp[i][j]
        return solve(m-1,n-1)
        
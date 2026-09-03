class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        dp=[[[-1 for _ in range(m)] for _ in range(m)] for _ in range(n)]
        def solve(i,j1,j2):
            if j1<0 or j1>m-1 or j2<0 or j2>m-1:
                return float('-inf')
            if i==n-1:
                if j1==j2:
                    return grid[i][j1]
                return grid[i][j1]+grid[i][j2]
            if dp[i][j1][j2]!=-1:
                return dp[i][j1][j2]
            maxi=0
            for new_j1 in range(-1,2):
                for new_j2 in range(-1,2):
                    if j1==j2:
                        ans=grid[i][j1]+solve(i+1,j1+new_j1,j2+new_j2)
                    else:
                        ans=grid[i][j1]+grid[i][j2]+solve(i+1,j1+new_j1,j2+new_j2)
                    maxi=max(maxi,ans)
            dp[i][j1][j2]=maxi
            return dp[i][j1][j2]
        return solve(0,0,m-1)
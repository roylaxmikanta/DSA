class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        dp=[[[-1 for _ in range(m)] for _ in range(m)] for _ in range(n)]
        for j1 in range(m):
            for j2 in range(m):
                if j1==j2:
                    dp[n-1][j1][j2]=grid[n-1][j1]
                else:
                    dp[n-1][j1][j2]=grid[n-1][j1]+grid[n-1][j2]
        for i in range(n-2,-1,-1):
            for j1 in range(m):
                for j2 in range(m):
                    maxi=0
                    for new_j1 in (-1,0,1):
                        for new_j2 in (-1,0,1):
                            if j1+new_j1<0 or j1+new_j1>=m or j2+new_j2<0 or j2+new_j2>=m:
                                ans=float('-inf')
                            elif j1==j2:
                                ans=grid[i][j1]+dp[i+1][j1+new_j1][j2+new_j2]
                            else:
                                ans=grid[i][j1]+grid[i][j2]+dp[i+1][j1+new_j1][j2+new_j2]
                            maxi=max(maxi,ans)
                    dp[i][j1][j2]=maxi
        return dp[0][0][m-1]
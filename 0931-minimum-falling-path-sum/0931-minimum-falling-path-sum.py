class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        prev=[-1]*n
        for j in range(n):
            prev[j]=matrix[n-1][j]
        for i in range(n-2,-1,-1):
            curr=[-1]*n
            for j in range(n):
                if j!=0:
                    left=matrix[i][j]+prev[j-1]
                else:
                    left=float('inf')
                if j!=n-1:
                    right=matrix[i][j]+prev[j+1]
                else:
                    right=float('inf')
                up=matrix[i][j]+prev[j]
                curr[j]=min(up,left,right)
            prev=curr
        return min(prev)
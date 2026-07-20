class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        array=[]
        m=len(grid)
        n=len(grid[0])
        for i in range(m):
            for j in range(n):
                array.append(grid[i][j])
        if k>m*n:
            k=k%(m*n)
        array=array[m*n-k:]+array[:m*n-k]
        answer= [[0] * n for _ in range(m)]
        x=0
        for i in range(m):
            for j in range(n):
                answer[i][j]=array[x]
                x+=1
        return answer
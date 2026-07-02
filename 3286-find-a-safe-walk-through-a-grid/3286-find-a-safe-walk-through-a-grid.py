from collections import deque
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m=len(grid)
        n=len(grid[0])
        health-=grid[0][0]
        if health<=0:
            return False
        q=deque([(0,0,health)])
        best=[[-1]*n for _ in range(m)]
        best[0][0]=health
        dirs=[(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            x,y,h=q.popleft()
            if (x,y)==(m-1,n-1):
                return True
            for dx,dy in dirs:
                nx=x+dx
                ny=y+dy
                if 0<=nx<m and 0<=ny<n:
                    nh=h-grid[nx][ny]
                    if nh>0 and nh>best[nx][ny]:
                        best[nx][ny]=nh
                        q.append((nx,ny,nh))
        return False
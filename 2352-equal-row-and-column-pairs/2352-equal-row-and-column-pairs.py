from collections import Counter
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        my_set=Counter() 
        for row in grid:
            my_set[tuple(row)]+=1
        for i in range(len(grid)):
            for j in range(i+1,len(grid)):
                grid[i][j],grid[j][i]=grid[j][i],grid[i][j]
        count=0
        for row in grid:
            if tuple(row) in my_set:
                count+=my_set[tuple(row)]
        return count
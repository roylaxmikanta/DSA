class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n=len(intervals)
        intervals.sort(key=lambda x:(x[0],-x[1]))
        covered = [False]*n
        for i in range(n):
            for j in range(i+1,n):
                if intervals[i][1]>=intervals[j][1]:
                    covered[j]=True
        return covered.count(False)
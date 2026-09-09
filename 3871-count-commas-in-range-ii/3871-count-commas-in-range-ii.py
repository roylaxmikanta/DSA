class Solution:
    def countCommas(self, n: int) -> int:
        count=0
        start=1000
        com=1
        while start<=n:
            end=min(n,start*1000-1)
            count+=(end-start+1)*com
            start*=1000
            com+=1
        return count
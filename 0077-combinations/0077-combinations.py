class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer=[]
        def solve(index,subset):
            if len(subset)>=k:
                answer.append(subset[:]) 
                return
            for i in range(index,n+1):
                subset.append(i)
                solve(i+1,subset)
                subset.pop()
        solve(1,[])
        return answer
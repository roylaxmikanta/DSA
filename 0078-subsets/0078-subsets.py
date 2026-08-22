class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer=[]
        def solve(index,subset):
            answer.append(subset[:])
            for i in range(index,len(nums)):
                subset.append(nums[i])
                solve(i+1,subset)
                subset.pop()
        solve(0,[])
        return answer
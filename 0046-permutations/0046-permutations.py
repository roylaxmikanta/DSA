class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==1:
            return [nums]
        answer=[]
        def solve(start):
            if start==len(nums):
                answer.append(nums[:])
            for i in range(start,len(nums)):
                nums[i],nums[start]=nums[start],nums[i]
                solve(start+1)
                nums[i],nums[start]=nums[start],nums[i]
        solve(0)
        return answer
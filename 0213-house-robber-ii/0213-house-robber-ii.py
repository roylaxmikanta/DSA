class Solution:
    def solve(self,nums):
        if len(nums)<3:
            return max(nums)
        prev=max(nums[1],nums[0])
        prev2=nums[0]
        for i in range(2,len(nums)):
            curr=max(prev,nums[i]+prev2)
            prev2=prev
            prev=curr
        return prev
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        return max(self.solve(nums[:-1]),self.solve(nums[1:]))

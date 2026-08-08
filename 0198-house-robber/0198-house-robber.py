class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<3:
            return max(nums)
        prev=max(nums[1],nums[0])
        prev2=nums[0]
        for i in range(2,len(nums)):
            curr=max(prev,nums[i]+prev2)
            prev2=prev
            prev=curr
        return prev
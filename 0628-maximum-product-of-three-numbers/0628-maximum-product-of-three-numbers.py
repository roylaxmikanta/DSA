class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        num1=nums[-1]
        num2=nums[-2]
        num3=nums[-3]
        if abs(nums[0])>nums[-3] and abs(nums[1])>nums[-2]:
            num2=nums[1]
            num3=nums[0]
        return max(num1*num2*num3,nums[0]*nums[1]*nums[-1],nums[0]*nums[1]*nums[2],nums[-1]*nums[-2]*nums[-3])
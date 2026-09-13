class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        curr=0
        for i in range(len(nums)):
            if i>0:
                curr+=nums[i-1]
            total-=nums[i]
            if curr==total:
                return i
        return -1
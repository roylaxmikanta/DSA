class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n=len(nums)
        nums=sorted(nums)
        if nums[n-1]!=n-1:
            return False
        for i in range(n):
            if i!=n-1 and nums[i]!=i+1:
                return False
        return True
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1 or len(set(nums))==1:
            return nums[0]
        mini=nums[0]
        i=0
        while(i<n):
            mini=min(mini,nums[0])
            nums=[nums[-1]]+nums[:-1]
            i+=1
        return mini
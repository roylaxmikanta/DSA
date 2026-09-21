class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        zeros=0
        ans=0
        r=0
        l=0
        while r<len(nums):
            if nums[r]==0:
                zeros+=1
            if zeros>k:
                if nums[l]==0:
                    zeros-=1
                l+=1
            if zeros<=k:
                ans=max(ans,r-l+1)
            r+=1
        return ans
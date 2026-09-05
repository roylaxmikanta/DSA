class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        maxes=[]
        maxi=float('-inf')
        for i in range(len(nums)):
            maxi=max(maxi,nums[i])
            maxes.append(maxi)
        minis=[-1]*len(nums)
        mini=float('inf')
        for i in range(len(nums)-1,-1,-1):
            mini=min(mini,nums[i])
            minis[i]=mini
        for i in range(len(nums)):
            if maxes[i]-minis[i]<=k:
                return i
        return -1
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumi=sum(nums)
        if sumi%2!=0:
            return False
        target=sumi//2
        dp=[[False]*(target+1) for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i][0]=True
        if nums[0]<=target:
            dp[0][nums[0]]=True
        for index in range(1,len(nums)):
            for total in range(0,target+1):
                pick=False
                if nums[index]<=target:
                    pick=dp[index-1][total-nums[index]]
                not_pick=dp[index-1][total]
                dp[index][total]=pick or not_pick
        return dp[len(nums)-1][target]
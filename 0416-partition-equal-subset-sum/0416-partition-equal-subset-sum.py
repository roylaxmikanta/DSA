class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumi=sum(nums)
        if sumi%2!=0:
            return False
        target=sumi//2
        dp=[[-1]*(target+1) for _ in range(len(nums))]
        def solve(index,target):
            if target==0:
                return True
            if index<0:
                return False
            if index==0:
                if nums[0]==target:
                    return True
            if dp[index][target]!=-1:
                return dp[index][target]
            if nums[index]>target:
                pick=False
            else:
                pick=solve(index-1,target-nums[index])
            not_pick=solve(index-1,target)
            dp[index][target]=pick or not_pick
            return dp[index][target]
        return solve(len(nums)-1,target)

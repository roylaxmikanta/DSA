class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumi=sum(nums)
        if sumi%2!=0:
            return False
        target=sumi//2
        prev=[False]*(target+1)
        prev[0]=True
        if nums[0]<=target:
            prev[nums[0]]=True
        for index in range(1,len(nums)):
            curr=[False]*(target+1)
            curr[0]=True
            for total in range(0,target+1):
                pick=False
                if nums[index]<=total:
                    pick=prev[total-nums[index]]
                not_pick=prev[total]
                curr[total]=pick or not_pick
            prev=curr
        return prev[target]
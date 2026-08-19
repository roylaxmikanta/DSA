class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        answer=set()
        for i in range(len(nums)):
            my_set=set()
            for j in range(i+1,len(nums)):
                temp=-(nums[i]+nums[j])
                if temp in my_set:
                    mou=[nums[i],nums[j],temp]
                    mou.sort()
                    answer.add(tuple(mou))
                my_set.add(nums[j])    

        return list(list(ans)for ans in answer)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)):
            if count<2 or nums[i]!=nums[count-2]:
                nums[count]=nums[i]
                count+=1
        return count
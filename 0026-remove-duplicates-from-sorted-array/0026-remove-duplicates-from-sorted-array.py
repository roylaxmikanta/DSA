class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count=1
        i=1
        while i<len(nums):
            if nums[i]!=nums[i-1]:
                nums[count]=nums[i]
                count+=1
            i+=1
        return count
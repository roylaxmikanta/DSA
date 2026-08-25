class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        my_set=set(nums)
        i=1
        while i*k in my_set:
            i+=1
        return i*k
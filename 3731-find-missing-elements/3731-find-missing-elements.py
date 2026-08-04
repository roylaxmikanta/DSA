class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        answer=[]
        for num in range(min(nums),max(nums)+1):
            if num not in set(nums):
                answer.append(num)
        return answer
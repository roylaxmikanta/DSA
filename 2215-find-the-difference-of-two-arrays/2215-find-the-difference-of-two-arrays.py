class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        answer=[[],[]]
        n1=set(nums1)
        n2=set(nums2)
        for num in n1:
            if num not in n2:
                answer[0].append(num)
        for num in n2:
            if num not in n1:
                answer[1].append(num)
        return answer
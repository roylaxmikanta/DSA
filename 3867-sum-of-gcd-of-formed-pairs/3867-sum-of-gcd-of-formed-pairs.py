from math import gcd
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        maxi=0
        n=len(nums)
        prefixGcd=[]

        for i in range(n):
            maxi=max(maxi,nums[i])
            prefixGcd.append(gcd(maxi,nums[i]))

        prefixGcd=sorted((prefixGcd))

        left=0
        right=len(prefixGcd)-1
        answer=0
        
        while left<right:
            if left==right:
                break
            answer+=gcd(prefixGcd[left],prefixGcd[right])
            left+=1
            right-=1
            
        return answer
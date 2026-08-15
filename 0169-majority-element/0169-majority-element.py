class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map={}
        for num in nums:
            if num not in hash_map:
                hash_map[num]=1
            else:
                hash_map[num]+=1
        return sorted(hash_map.items(),key=lambda x:x[1],reverse=True)[0][0]
        
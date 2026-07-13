class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        hash_map={}
        my_set=sorted(set(arr))
        for i,num in enumerate(my_set):
            hash_map[num]=i+1
        answer=[]
        for key in arr:
            answer.append(hash_map[key])
        return answer
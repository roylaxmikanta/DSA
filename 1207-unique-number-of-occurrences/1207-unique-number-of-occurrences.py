class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        hash_MAP={}
        for i in range(len(arr)):
            if arr[i] not in hash_MAP:
                hash_MAP[arr[i]]=1
            else:
                hash_MAP[arr[i]]+=1
        my_set=set()
        for key in hash_MAP:
            if hash_MAP[key] not in my_set:
                my_set.add(hash_MAP[key])
            else:
                return False
        return True
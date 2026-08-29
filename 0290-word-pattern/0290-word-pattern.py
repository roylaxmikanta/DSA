class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hash_map1={}
        hash_map2={}
        new=s.split()
        if len(pattern)!=len(new):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in hash_map1:
                hash_map1[pattern[i]]=new[i]
            if new[i] not in hash_map2:
                hash_map2[new[i]]=pattern[i]
            if pattern[i] in hash_map1 and hash_map1[pattern[i]] != new[i]:
                return False
            if new[i] in hash_map2 and hash_map2[new[i]]!=pattern[i]:
                return False
        return True
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hash_map1={}
        hash_map2={}
        for i in range(len(s)):
            if s[i] not in hash_map1:
                hash_map1[s[i]]=t[i]
            else:
                if hash_map1[s[i]]!=t[i]:
                    return False
            if t[i] not in hash_map2:
                hash_map2[t[i]]=s[i]
            else:
                if hash_map2[t[i]]!=s[i]:
                    return False
        return True
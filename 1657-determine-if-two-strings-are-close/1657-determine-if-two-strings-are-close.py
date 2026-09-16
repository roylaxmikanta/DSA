class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return False
        hash_map={}
        hash_map2={}
        for i in range(len(word1)):
            if word1[i] not in hash_map:
                hash_map[word1[i]]=1
            else:
                hash_map[word1[i]]+=1
            if word2[i] not in hash_map2:
                hash_map2[word2[i]]=1
            else:
                hash_map2[word2[i]]+=1
        my_set1=set()
        arr1=[]
        for key in hash_map:
            arr1.append(hash_map[key])
            my_set1.add(key)
        my_set2=set()
        arr2=[]
        for key in hash_map2:
            arr2.append(hash_map2[key])
            my_set2.add(key)
        arr1.sort()
        arr2.sort()
        if arr1!=arr2 or my_set1!=my_set2:
            return False
        return True
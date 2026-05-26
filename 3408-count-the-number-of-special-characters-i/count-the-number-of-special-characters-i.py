class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        small=[0]*26
        cap=[0]*26
        for alp in word:
            no=ord(alp)
            if(no<97 and cap[no-65]==0):
                cap[no-65]=1
            if(no>=97 and small[no-97]==0):
                small[no-97]=1
        count=0
        for i in range(26):
            if (small[i]+cap[i]==2):
                count+=1
        return count
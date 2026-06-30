class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count={'a':0,'b':0,'c':0}
        left=0
        ans=0
        n=len(s)
        for i in range(n):
            count[s[i]]+=1
            while count['a']>0 and count['b']>0 and count['c']>0: 
                ans+=n-i
                count[s[left]]-=1
                left+=1
        return ans
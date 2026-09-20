class Solution:
    def reverseDegree(self, s: str) -> int:
        ans=0
        for i in range(len(s)):
            no=26-ord(s[i])+97
            ans+=((i+1)*no)
        return ans
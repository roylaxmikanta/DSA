class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==1:
            return s
        half=len(s)//2
        s="".join(sorted(s[:half]))+s[half:]
        left=0
        right=len(s)-1
        s=list(s)
        while(left<right):
            s[right]=s[left]
            left+=1
            right-=1
        return "".join(s)
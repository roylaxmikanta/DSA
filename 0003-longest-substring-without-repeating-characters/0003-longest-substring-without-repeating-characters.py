class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slow=0
        fast=0
        maxi=0
        my_set=set()
        while fast<len(s):
            if s[fast] not in my_set:
                my_set.add(s[fast])
                maxi=max(maxi,fast-slow+1)
            else:
                while len(my_set)!=0 and s[fast] in my_set:
                    my_set.remove(s[slow])
                    slow+=1
                my_set.add(s[fast])
            fast+=1
        return maxi
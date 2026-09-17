class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel={'a','e','i','o','u'}
        left=0
        right=k
        count=0
        maxi=0
        for i in range(k):
            if s[i] in vowel:
                count+=1
        maxi = count
        while right<len(s):
            if s[right] in vowel:
                count+=1
                right+=1
            else:
                right+=1
            if s[left] in vowel:
                count-=1
                left+=1
            else:
                left+=1
            maxi=max(count,maxi)
        return maxi

        
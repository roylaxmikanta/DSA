class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        x=len(needle)
        if haystack==needle:
            return 0
        for o in range(len(haystack)-x+1):
            if(needle==haystack[o:o+x]):
                return o
        return -1
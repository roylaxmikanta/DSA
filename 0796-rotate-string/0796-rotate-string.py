class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)==len(goal):
            new_s=s+s
            if goal in new_s:
                return True
        return False
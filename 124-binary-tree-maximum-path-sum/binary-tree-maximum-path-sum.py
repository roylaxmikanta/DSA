# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi=float("-inf")
        def solve(root):
            nonlocal maxi
            if root is None:
                return 0
            LS=solve(root.left)
            if(LS<0):
                LS=0
            RS=solve(root.right)
            if(RS<0):
                RS=0
            maxi=max(maxi,root.val+LS+RS)
            return root.val+max(LS,RS)
        solve(root)
        return maxi
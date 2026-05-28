# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer=[]
        def solve(root):
            if root:
                if root.left:
                    solve(root.left)
                if root.right:
                    solve(root.right)
                if root:
                    answer.append(root.val)
        solve(root)
        return answer
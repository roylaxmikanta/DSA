# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        answer=[]
        def solve(root,level):
            if root is None:
                return 
            if len(answer)==level:
                answer.append(root.val)
            if root.right:
                solve(root.right,level+1)
            if root.left:
                solve(root.left,level+1)
        solve(root,0)
        return answer
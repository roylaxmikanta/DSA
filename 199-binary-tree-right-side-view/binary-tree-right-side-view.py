# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def solve(root,level,answer):
            if root is None:
                return 
            if(len(answer)==level):
                answer.append(root.val)
            if(root.right):
                solve(root.right,level+1,answer)
            if(root.left):
                solve(root.left,level+1,answer)
        answer=[]
        solve(root,0,answer)
        return answer
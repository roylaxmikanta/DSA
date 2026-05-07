# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter=0
        def calculateHeight(root):
            nonlocal diameter
            if root is None:
                return 0  
            left_root=calculateHeight(root.left)
            right_root=calculateHeight(root.right)
            diameter=max(diameter,left_root+right_root)
            return 1+max(left_root,right_root)
        calculateHeight(root)
        return diameter
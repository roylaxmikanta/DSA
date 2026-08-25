# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return [0]
        answer=[]
        queue=deque([])
        queue.append(root)
        answer=[]
        while len(queue)!=0:
            total=0
            count=0
            for _ in range(len(queue)):
                e=queue.popleft()
                total+=(e.val)
                count+=1
                if e.left:
                    queue.append(e.left)
                if e.right:
                    queue.append(e.right)
            answer.append(total/count)
        return answer
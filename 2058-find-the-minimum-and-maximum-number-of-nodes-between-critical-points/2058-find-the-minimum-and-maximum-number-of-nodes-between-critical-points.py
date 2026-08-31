# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev=head
        curr=head.next
        max_min=[]
        i=2
        while curr and curr.next:
            front=curr.next
            if prev.val<curr.val>front.val or prev.val>curr.val<front.val:
                max_min.append(i)
            i+=1
            prev=curr
            curr=front
        if len(max_min)<2:
            return [-1,-1]
        mini=float('inf')
        for i in range(1,len(max_min)):
            mini=min(mini,max_min[i]-max_min[i-1])
        return [mini,max_min[-1]-max_min[0]]
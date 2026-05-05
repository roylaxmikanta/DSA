# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        length=0
        temp=head
        while(temp is not None):
            length+=1
            temp=temp.next
        if((k%length)==0):
            return head
        c=length-(k%length)
        t=0
        pre_head=head
        curr=head
        while(t<c):
            prev=curr
            curr=curr.next
            t+=1
        new_head=curr
        prev.next=None
        while(curr.next is not None):
            curr=curr.next
        curr.next=pre_head
        return new_head
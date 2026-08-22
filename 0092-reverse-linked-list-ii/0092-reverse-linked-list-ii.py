# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None or head.next is None or left==right:
            return head
        count=1
        head1=head
        while head and count!=left:
            count+=1
            p=head
            head=head.next
        prev=head
        p2=prev
        temp=head.next
        while count!=right and temp:
            front=temp.next
            temp.next=prev
            prev=temp
            temp=front
            count+=1
        if left!=1:
            p.next=prev
        p2.next=temp
        if left!=1:
            return head1
        else:
            return prev
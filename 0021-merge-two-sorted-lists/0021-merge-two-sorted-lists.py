# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        new=ListNode(-1)
        head=new
        while list1 and list2:
            if list1.val<=list2.val:
                new.next=ListNode(list1.val)
                list1=list1.next
            else:
                new.next=ListNode(list2.val)
                list2=list2.next
            new=new.next
        if list1:
            new.next=list1
        if list2:
            new.next=list2
        return head.next
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        my_set=set()
        curr=headA
        while curr:
            my_set.add(curr)
            curr=curr.next
        temp=headB
        while temp:
            if temp in my_set:
                return temp
            temp=temp.next
        return None
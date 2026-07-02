# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        rv = slow.next # create the second half from middle to the end
        slow.next = None # creates the first half tail by pointing to None
        prev=None
        while rv:
            next=rv.next
            rv.next=prev
            prev=rv
            rv=next
        first=head
        second=prev

        while first and second:
            
            first_next=first.next
            second_next=second.next
            first.next=second
            second.next=first_next

            first=first_next
            second=second_next


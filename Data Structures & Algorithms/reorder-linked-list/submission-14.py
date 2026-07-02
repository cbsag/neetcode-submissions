# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=head
        fast=head.next

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        reverse= slow.next
        slow.next=None
        prev=None
        while reverse:
            nxt=reverse.next
            reverse.next=prev
            prev=reverse
            reverse=nxt
        
        first=head
        second=prev

        while first and second:
            first_next=first.next
            second_next=second.next

            first.next=second
            second.next=first_next

            first=first_next
            second=second_next

























        # # first find the middle value to cut the list into two halves
        # # then we can reverse the second halve and merge two lists based on the logi one from the first and next from the second

        # slow=head
        # fast=head.next
        # while fast and fast.next:
        #     slow=slow.next
        #     fast=fast.next.next
        # rv = slow.next # create the second half from middle to the end
        # slow.next = None # creates the first half tail by pointing to None
        # #reversing the second list
        # prev=None
        # while rv:
        #     next=rv.next
        #     rv.next=prev
        #     prev=rv
        #     rv=next
        # first=head
        # second=prev
        # # merging two halves into one using the logic

        # while first and second:
            
        #     first_next=first.next
        #     second_next=second.next
        #     first.next=second
        #     second.next=first_next

        #     first=first_next
        #     second=second_next


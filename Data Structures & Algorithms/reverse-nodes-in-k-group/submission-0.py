# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        groupPrev=dummy
        while True:
            kth=groupPrev
            for _ in range(k):
                kth=kth.next
                if not kth:
                    return dummy.next
            groupNext=kth.next
            #Reverse
            tmp=groupPrev.next
            curr=groupPrev.next
            prev=groupNext

            while curr!=groupNext:
                next=curr.next
                curr.next=prev
                prev=curr
                curr=next

            groupPrev.next=prev
            groupPrev=tmp
        return dummy.next
            
        
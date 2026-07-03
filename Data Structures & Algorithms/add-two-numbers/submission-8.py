# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        total=0
        store=0
        carry=0
        #base is 10 (0-9)

        dummy=ListNode()
        tail=dummy

        while l1 or l2 or carry:
            l1v=l1.val if l1 else 0
            l2v=l2.val if l2 else 0

            total = l1v+l2v+carry
            store=total%10
            carry=total// 10
            tail.next=ListNode(store)
            tail=tail.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return dummy.next        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # store=0
        # carry=0
        # total=0
        # dummy=ListNode()
        # tail=dummy

        # while l1 or l2 or carry:
        #     l1_val=l1.val if l1 else 0
        #     l2_val=l2.val if l2 else 0

        #     total=l1_val+l2_val+carry
        #     store=total%10
        #     carry=total//10
        #     res=ListNode(store)
        #     tail.next=res
        #     tail=tail.next

        #     if l1:
        #         l1=l1.next
        #     if l2:
        #         l2=l2.next
        # return dummy.next
        
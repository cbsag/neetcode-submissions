# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail =dummy
        
        while list1 and list2:
            if list1.val<=list2.val:
                tail.next=list1
                list1=list1.next
                tail=tail.next
            else:
                tail.next=list2
                list2=list2.next
                tail=tail.next
        if list1:
            tail.next=list1
            #shouldnt i do tail=tai.next here?
        else:
            tail.next=list2
        return dummy.next


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # dummy = ListNode()
        # tail= dummy
        # current_1=list1
        # current_2=list2
        # while current_1 and current_2:
        #     if current_1.val <= current_2.val:
        #         tail.next=current_1
        #         current_1=current_1.next
        #         tail=tail.next
                
        #     else:
        #         tail.next=current_2
        #         current_2=current_2.next
        #         tail=tail.next
        # if current_1:
        #     tail.next=current_1
        # else:
        #     tail.next=current_2

        # return dummy.next
        # p1 = list1
        # p2 = list2

        # temp_node = ListNode(0)
        # tail= temp_node
        # while p1 and p2:
        #     if p1.val<=p2.val:
        #         tail.next = p1
        #         p1=p1.next
        #     else:
        #         tail.next = p2
        #         p2=p2.next
        #     tail=tail.next
        # if p1:
        #     tail.next=p1
        # else:
        #     tail.next=p2
        # return temp_node.next
        
        # print(l1_curr.val,l2_curr.val)

       




        
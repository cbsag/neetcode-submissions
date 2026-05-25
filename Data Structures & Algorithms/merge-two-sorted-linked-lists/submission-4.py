# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2

        temp_node = ListNode(0)
        tail= temp_node
        while p1 and p2:
            if p1.val<=p2.val:
                tail.next = p1
                p1=p1.next
            else:
                tail.next = p2
                p2=p2.next
            tail=tail.next
        if p1:
            tail.next=p1
        else:
            tail.next=p2
        return temp_node.next
        
        # print(l1_curr.val,l2_curr.val)
        '''
        1: I can convert linked list to a list and sort them and then convert to a new linked list
        2: I can use a temp node to store and attach it to the tail by comparsion (p1.val <=p2.val) aka pointers voila
        '''

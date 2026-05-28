# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # curr = head
        # new_head = None

        # while curr:
        #     # print(curr.val)
        #     new_node= ListNode(curr.val)
        #     # print(new_node)
        #     new_node.next=new_head
        #     new_head = new_node
        #     curr = curr.next
        #     # print(curr.next)
        # return new_head


        curr = head
        new_head =None
        
        '''
        curr
        1->2 2->3 3->4

        new_node
        1 -> None


        curr.val is 1
        new_code is 1
        new_code.next is 1
        curr.next is 2
        '''
        while curr:
            new_node=ListNode(curr.val)
            new_node.next=new_head
            new_head = new_node
            curr = curr.next
        return new_head

































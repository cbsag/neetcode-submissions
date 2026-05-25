# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        new_head = None

        while curr:
            # print(curr.val)
            new_node= ListNode(curr.val)
            # print(new_node)
            new_node.next=new_head
            new_head = new_node
            curr = curr.next
            # print(curr.next)
        return new_head
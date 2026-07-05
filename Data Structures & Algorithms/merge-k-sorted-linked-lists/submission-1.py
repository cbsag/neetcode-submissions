# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy=ListNode()
        tail=dummy
        # min_node= None
        # min_index=-1

        while any(lists):
            min_node= None
            min_index=-1
            for i in range(len(lists)):
                if lists[i] is None:
                    continue
                if min_node is None or lists[i].val <min_node.val:
                    min_node=lists[i]
                    min_index=i
            tail.next=min_node
            tail=tail.next
            lists[min_index]=lists[min_index].next
        return dummy.next

                

            
            
        
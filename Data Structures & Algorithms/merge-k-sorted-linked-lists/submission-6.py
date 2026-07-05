# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # dummy=ListNode()
        # tail=dummy
        # # min_node= None
        # # min_index=-1

        # while any(lists):
        #     min_node= None
        #     min_index=-1
        #     for i in range(len(lists)):
        #         if lists[i] is None:
        #             continue
        #         if min_node is None or lists[i].val <min_node.val:
        #             min_node=lists[i]
        #             min_index=i
        #     tail.next=min_node
        #     tail=tail.next
        #     lists[min_index]=lists[min_index].next
        # return dummy.next
        # time is O(N*K)

        #Min heap

        import heapq
        dummy=ListNode()
        tail=dummy
        heap =[]
        # print(heap)
        for i in range(len(lists)):
            if lists[i] is None:
                continue
            heapq.heappush(heap,(lists[i].val,i,lists[i]))


        while heap:
            val,i,node=heapq.heappop(heap)
            tail.next=node
            tail=tail.next

            if node.next:
                heapq.heappush(heap,(node.next.val,i,node.next))
        return dummy.next


        # print(heap)

                

                

            
            
        
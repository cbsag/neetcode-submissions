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

        # import heapq
        # dummy=ListNode()
        # tail=dummy
        # heap =[]
        # # print(heap)
        # for i in range(len(lists)):
        #     if lists[i] is None:
        #         continue
        #     heapq.heappush(heap,(lists[i].val,i,lists[i]))

        # heap sloves the min value conditon
        # while heap:
        #     val,i,node=heapq.heappop(heap)
        #     tail.next=node
        #     tail=tail.next

        #     if node.next:
        #         heapq.heappush(heap,(node.next.val,i,node.next))
        # return dummy.next


        # print(heap)

        #Divide and Conquer
        if not lists:
            return None
        while len(lists)>1:
            mergedLists=[]

            for i in range(0,len(lists),2):
                l1=lists[i]
                l2=lists[i+1] if i+1 <len(lists) else None
                mergedLists.append(self.merge(l1,l2))

            lists=mergedLists
        return lists[0]
            


                
    def merge(self,list1,list2 ):
        dummy=ListNode()
        tail=dummy
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
        else:
            tail.next=list2

        return dummy.next
                

            
            
        
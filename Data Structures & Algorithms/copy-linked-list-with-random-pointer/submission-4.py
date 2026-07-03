"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        3 -> 7 -> 4 -> 5 -> null

        copied node:
        origonal val of the copied node
        we need to know the copoied nodes current val,next and the random value:
            the current.next should point to the same next similar to the origonal node
        
        From this I can undersatnd that I have to create a map:

        old node:  copied node 
        val,next,random : val,next,random

        first I need to ceate copy of the nodes and then map the next and random right..

        so I create a dummy=head
        """

        curr=head
        old_to_copy={None:None}

        while curr:
            copy=Node(curr.val)
            old_to_copy[curr]=copy
            curr=curr.next
        
        curr=head

        while curr:
            copied=old_to_copy[curr]

            copy_next=curr.next
            copy_random=curr.random
            copied.next=old_to_copy[copy_next]
            copied.random=old_to_copy[copy_random]
            curr=curr.next
        return old_to_copy[head]






















        # curr=head
        # old_to_copy = {None: None}

        # while curr:
        #     copy=Node(curr.val)
        #     old_to_copy[curr]=copy
        #     curr=curr.next
        # curr=head
        # while curr:
        #     copied=old_to_copy[curr]
        #     copy_next=curr.next
        #     copy_random=curr.random
        #     copied.next=old_to_copy[copy_next]
        #     copied.random =old_to_copy[copy_random]

        #     curr=curr.next
        # return old_to_copy[head]


        
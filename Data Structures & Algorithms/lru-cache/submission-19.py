class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val

        self.prev=None
        self.next=None



class LRUCache:

    def __init__(self, capacity: int):
        self.cache={}
        self.cap=capacity

        # I need to create LRU
        self.left=Node(0,0)
        self.right=Node(0,0)


        self.left.next=self.right
        self.right.prev=self.left

    def remove(self,node):
        prev_node=node.prev
        next_node=node.next

        prev_node.next=next_node
        next_node.prev=prev_node

    def insert(self,node):
        prev_node=self.right.prev
        next_node=self.right

        prev_node.next=node
        node.prev=prev_node

        node.next=next_node
        next_node.prev=node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node=self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val

        


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node=self.cache[key]
            node.val=value
            self.remove(node)
            self.insert(node)
        else:
            node= Node(key,value)
            self.cache[key]=node
            self.insert(node)
        if len(self.cache)>self.cap:
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]




















# class Node:
#     def __init__(self,key,val):
#         self.key=key
#         self.val=val
#         self.prev=None
#         self.next=None


# class LRUCache:

#     def __init__(self, capacity: int):
#         self.cache={}
#         self.cap=capacity
        
#         self.left=Node(0,0)
#         self.right=Node(0,0)
        
#         self.left.next=self.right
#         self.right.prev=self.left
        

#     def get(self, key: int) -> int:
#         if key not in self.cache:
#             return -1
#         node=self.cache[key]
#         self.remove(node)
#         self.insert(node)
#         return node.val


#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             node=self.cache[key]
#             node.val=value
#             self.remove(node)
#             self.insert(node)
#         else:
#             node= Node(key,value)
#             self.cache[key]=node
#             self.insert(node)
#         if len(self.cache)>self.cap:
#             lru=self.left.next
#             self.remove(lru)
#             del self.cache[lru.key]


    
#     def remove(self,node):
#         prev_node=node.prev
#         next_node=node.next

#         prev_node.next=next_node
#         next_node.prev=prev_node
    
#     def insert(self,node):
#         prev_node=self.right.prev
#         next_node=self.right

#         prev_node.next=node
#         node.prev=prev_node

#         node.next=next_node
#         next_node.prev=node

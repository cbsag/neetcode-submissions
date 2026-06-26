class MinStack:

    def __init__(self):
        self.stack=[]
        self.mstack=[]
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mstack:
            self.mstack.append(val)
        else:
            self.mstack.append(min(val,self.mstack[-1]))


        

    def pop(self) -> None:
        self.stack.pop()
        self.mstack.pop()

   

    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.mstack[-1]
      
        


#     push = appending to a stack

#    '''
#     1
#     1
#     2
#     3
#     4
#     LIFO
#     PUSH-> append to the list
#     pop-> 
# '''
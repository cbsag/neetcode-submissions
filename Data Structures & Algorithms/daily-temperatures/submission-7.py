class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        stack will ahve indicies 
        for each temprature add their indices to the stack
        as I read the first temparture if the stack is empty I push that indice to the stack.

    then else:
    stack is not empty .. whle loop where i chekc if current_temparyure > temp at the stack top(stack[-1]):
    pop old_index
    calcalte the asnwer which current_inde-old_index
    push the current_index to tht stack?

        '''
        # monotonic stack woudl only store the indeies of the 
        stack=[]
        result=[0]* len(temperatures)
        current_temp=0
        for i in range(len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                old=stack.pop()
                result[old]=i-old
            stack.append(i)
        return result

            # current_temp=tempratures[i]
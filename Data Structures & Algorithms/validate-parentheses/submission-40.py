class Solution:
    def isValid(self, s: str) -> bool:
        '''
        use a stack for opening bracket
        when I see a closing rbakcet it must match the most recent openeing bracket
        if it does not match, return False
        at th end , stack must be empty


        [ ]
        '''
        stack=[]
        brac={
            ")":"(",
            "}":"{",
            "]":"["
        }
        for val in s:
            # print(val)
            if not s:
                return False
            if val not in brac:
                stack.append(val)
            else:
                if not stack:
                    return False

                if brac[val]!=stack.pop():
                    return False
                
                        
                    # print("inside else")
                    # return False
            
       
        return not stack
        
 

















class Solution:
    def isValid(self, s: str) -> bool:
        # stack = []
        # pairs = {
        #     ")": "(",
        #     "}": "{",
        #     "]": "["
        # }

        # if len(s)==1:
        #     return False
        # for char in s:
        #     if char not in pairs:
        #         stack.append(char)
        #     else:
        #         if not(stack):
        #             return False
                
        #         last_open = stack.pop()
        #         if last_open != pairs[char]:
        #             return False
        # return not stack
        
        stack=[]
        pairs={")":"(","}":"{","]":"["}

        if len(s)==1:
            return False
        for char in s:
            if char not in pairs:
                stack.append(char)
            else:
                if not stack:
                    return False
                last_open=stack.pop()

                if last_open != pairs[char]:
                    return False
        return not stack



















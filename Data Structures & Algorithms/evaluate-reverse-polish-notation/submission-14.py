class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operators = {'+', '-', '*', '/',}

        for i in range(len(tokens)):
            if tokens[i] not in operators:
                stack.append(tokens[i])
            else:
                second=int(stack.pop())
                first=int(stack.pop())

                if tokens[i]=="+":
                    stack.append(first+second)
                elif tokens[i]=="-":
                    stack.append(first-second)
                elif tokens[i]=="*":
                    stack.append(first*second)
                elif tokens[i]=="/":
                    stack.append(int(first/second))
        return int(stack[0])




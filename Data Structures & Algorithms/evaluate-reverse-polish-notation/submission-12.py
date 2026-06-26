class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        number
        operator
        if token is a number:
            add to stack
        if token is "+" :
            num1=number.pop()
            num2=number.pop()
            res=num1+num2
            number.appen(res)
        if token is"*":
            do the same
        if token os "-"
        num2=pop()
        num1=pop()
        res=num1-num2
        if token is "/"
        same
                '''
        stack=[]
        # operators = {'+', '-', '*', '/',}

        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))
            if token == "+":
                num1=stack.pop()
                num2=stack.pop()
                res=num1+num2
                stack.append(res)
            if token == "*":
                num1=stack.pop()
                num2=stack.pop()
                res=num1*num2
                stack.append(res)
            if token == "-":
                num2=stack.pop()
                num1=stack.pop()
                res=num1-num2
                stack.append(res)
            if token == "/":
                num2=stack.pop()
                num1=stack.pop()
                res=int(num1/num2)
                stack.append(res)
            # print(stack)
        return stack[0]

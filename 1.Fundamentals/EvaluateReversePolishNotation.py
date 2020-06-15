import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # iterate through input and add it to stack
        
        # case 1: operator
            # start poping last two element
            # perform the operation
            # add the result to stack
        # case 2: number
            # add to stack
            
        stack = []
        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                num2, num1 = stack.pop(), stack.pop()
                result = eval("{}{}{}".format(num1, token, num2))
                stack.append(math.trunc(result))
            else:
                stack.append(token)
            #print("Token:{} Stack: {}".format(token, stack))
            
        # pop from stack
        return stack.pop()

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        mydict = {"*", "+", "-", "/"}
        result = 0
        for i in range(len(tokens)):
            if tokens[i] not in mydict:
                stack.append(tokens[i])
            elif tokens[i] in mydict:
                firstNo = int(stack.pop())
                if (tokens[i] == "+"):
                    result = int(stack.pop()) + firstNo
                elif (tokens[i] == "*"):
                    result = int(stack.pop()) * firstNo
                elif (tokens[i] == "-"):
                    result = int(stack.pop()) - firstNo
                else:
                    second = int(stack.pop())
                    result = abs(second) // abs(firstNo)
                    if(second < 0 and firstNo > 0) or (second > 0 and firstNo < 0):                     
                        result *= -1
                stack.append(result)    
        return stack[0]
                
                
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                a, b = stack.pop(), stack.pop()
                stack.append(b+a)
            elif token == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif token == "*":
                a, b = stack.pop(), stack.pop()
                stack.append(b*a)
            elif token == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(token))
        return stack[0]
    
s = Solution()
print(s.evalRPN(tokens = ["2","1","+","3","*"]))
print(s.evalRPN(tokens = ["4","13","5","/","+"]))
print(s.evalRPN(tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

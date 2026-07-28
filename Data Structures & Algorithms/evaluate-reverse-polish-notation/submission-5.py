class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                right = stack.pop()
                left = stack.pop()
                stack.append(left + right)
            elif c == "-":
                right = stack.pop()
                left = stack.pop()
                stack.append(left - right)
            elif c == "*":
                right = stack.pop()
                left = stack.pop()
                stack.append(left * right)
            elif c == "/":
                right = stack.pop()
                left = stack.pop()
                # Assume that division between integers always truncates toward zero.
                stack.append(int(left / right))
            else:
                stack.append(int(c))
            print(stack)
        return stack.pop()
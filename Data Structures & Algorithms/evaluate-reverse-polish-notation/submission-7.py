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
                # (6//132) = -1, but req is to truncate instead of round
                stack.append(int(left / right))
            else:
                stack.append(int(c))
        return stack.pop()
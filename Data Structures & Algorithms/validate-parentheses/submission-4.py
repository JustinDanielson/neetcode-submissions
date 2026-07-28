class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left_syntax_set = set(["(", "{", "["])
        for c in s:
            if c in left_syntax_set:
                stack.append(c)
            elif len(stack) > 0:
                if c == ")" and stack[-1] == "(":
                    stack.pop()
                elif c == "}" and stack[-1] == "{":
                    stack.pop()
                elif c == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            else:
                return False
        return len(stack) == 0
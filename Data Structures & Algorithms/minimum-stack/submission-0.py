class MinStack:
    # pop pops the last element inserted, but top will return the smallest known element
    def __init__(self):
        self.min_history = []
        self.stack = []

    def push(self, val: int) -> None:
        # To make this O(1), we should use 2 stacks
        # One to hold the elements and another that is the minimum item during each push
        self.stack.append(val)
        if len(self.min_history) == 0 or val < self.min_history[-1]:
            self.min_history.append(val)
        elif val >= self.min_history[-1]:
            self.min_history.append(self.min_history[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.min_history.pop()

    def top(self) -> int:
        return self.stack[-1] if len(self.stack) > 0 else None

    def getMin(self) -> int:
        return self.min_history[-1] if len(self.min_history) > 0 else None
        

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures and len(temperatures) == 0:
            return []

        min_stack = []
        res = [0] * len(temperatures)
        for i in range(len((temperatures))):
            while min_stack and temperatures[i] > temperatures[min_stack[-1]]:
                res[min_stack[-1]] = i - min_stack[-1]
                min_stack.pop()
            min_stack.append(i) # current temp is now <= top of stack
        # Anything left in min_stack has no greater temp in future temps
        return res
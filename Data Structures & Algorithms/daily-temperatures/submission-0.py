class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures and len(temperatures) == 0:
            return []

        res = [0]
        max_stack = [[len(temperatures) - 1, temperatures[-1]]]
        # Traverse temperatures backwards
        i = len(temperatures) - 2
        while i >= 0:
            num_days, found, temp = 0, False, temperatures[i]
            # For each temperature seen, pop all smaller or equal temps in max_stack
            # monotonic stack where top is >= all prev temps
            while not found and len(max_stack) > 0:
                if temp >= max_stack[-1][1]:
                    max_stack.pop()
                else:
                    num_days = max_stack[-1][0] - i
                    max_stack.append([i, temp])
                    found = True
            if not found:
                max_stack.append([i, temp])
            i -= 1
            res.append(num_days if found else 0)
        return list(reversed(res))
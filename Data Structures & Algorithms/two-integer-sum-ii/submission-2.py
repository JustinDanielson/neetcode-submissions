class Solution:
    # Your solution must use O(1) additional space.
    # Return the indices (1-indexed) of two numbers, [index1, index2], 
    # such that they add up to a given target number target and index1 < index2. 
    # Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        cur_sum = numbers[l] + numbers[r]

        while cur_sum != target and l < r:
            if cur_sum < target:
                l += 1
            elif cur_sum > target:
                r -= 1
            cur_sum = numbers[l] + numbers[r]
        if cur_sum == target:
            return [l + 1,r + 1]
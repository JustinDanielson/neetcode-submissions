class Solution:
    def search(self, nums: List[int], target: int) -> int:
        elements_remaining = count = len(nums)
        i = len(nums) >> 1
        while i < count and i >= 0 and elements_remaining > 0:
            elements_remaining >>= 1
            step = (elements_remaining // 2) + (elements_remaining & 1)
            if nums[i] > target:
                i = i - step
            elif nums[i] < target:
                i = i + step
            else:
                return i
        return -1
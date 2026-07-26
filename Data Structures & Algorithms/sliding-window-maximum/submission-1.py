class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = list()
        high_idx = -1
        for i in range(len(nums) - k + 1):
            if i > high_idx:
                res.append(max(nums[i: i + k]))
                high_idx = nums.index(res[-1])
            else:
                new_num = nums[i + k - 1]
                if new_num > res[-1]:
                    high_idx = i + k - 1
                    res.append(new_num)
                else:
                    res.append(res[-1])
        return res

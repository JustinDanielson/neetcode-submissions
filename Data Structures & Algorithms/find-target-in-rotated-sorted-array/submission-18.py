class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        k = 0 #rotation count
        m = 0 #midpoint

        # handle null input
        if not nums:
            return -1
        # handle len 1 or 2
        if len(nums) <= 2:
            if nums[0] == target:
                return 0
            elif len(nums) == 2 and nums[1] == target:
                return 1
            return -1
        
        # there exists a k where nums[k] < nums[k-1], this is the rotation amount
        if nums[0] < nums[-1]: #already sorted
            k = 0
        else:
            k = (l + r) // 2
            while nums[k] > nums[k-1]:
                if nums[0] >= nums[k]:
                    r = k
                else:
                    l = k + 1
                k = (l + r) // 2
        
        # there exists a nums[k + m] where nums[k + m] == target, 0 <= m <= len(nums)
        l, r = 0, len(nums) - 1
        m = (l + r) // 2
        while l <= r:
            idx = (m + k) % len(nums)
            if nums[idx] == target:
                return idx
            elif nums[idx] > target:
                r = m - 1
            else:
                l = m + 1
            m = (l + r) // 2
        return -1
            


                
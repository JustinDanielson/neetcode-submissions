class Solution:
    # One-liner
    # def hasDuplicate(self, nums: List[int]) -> bool:
    #     return len(set(nums)) != len(nums)
    
    # Space optimized O(n)
    def hasDuplicate(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums) - 1):
            if sorted_nums[i] == sorted_nums[i+1]:
                return True
        return False

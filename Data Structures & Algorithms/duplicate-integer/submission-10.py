class Solution:
    # One-liner
    # def hasDuplicate(self, nums: List[int]) -> bool:
    #     return len(set(nums)) != len(nums)
    
    # Space optimized
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort() #in-place sort
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return True
        return False
class Solution:
    # Assumption is that nums is sorted and only positive
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     left, right = 0, len(nums) - 1
    #     while True:
    #         total = nums[left] + nums[right]
    #         if total == target:
    #             return [left, right]
    #         elif total > target:
    #             right -= 1
    #         elif total < target:
    #             left += 1

    # Works with unsorted and negative
    # List can have duplicate values [3,3] w/ target = 6
    # List can have negatives
    # List will always contain an answer
    # Because this is only twoSum, the dict comprehension may have {3:0} and {3:1}, but it is okay because
    # the linear scan is going left to right, so the num_table will always contain the later index of the 2nd '3'
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_table = {nums[i]: i for i in range(len(nums))}
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in num_table and num_table[remainder] != i:
                return [i, num_table[remainder]]
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        right = [1]
        # Compute the product of all numbers going from left and right
        # and right to left. For any i, left[i] * right[i] will be
        # nums[0] * ... * nums[i-1]
        # nums[n] * ... * nums[i+1]
        # nums[i] will be missing from each
        for i in range(1, len(nums)):
            left.append(left[i-1] * nums[i-1])
            right.append(right[i-1] * nums[-i])
        right = right[::-1]
        res = [a * b for a,b in list(zip(left, right))]
        return res
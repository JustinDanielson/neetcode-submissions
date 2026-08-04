class Solution:
    # You are given an array of length n which was originally sorted in ascending order. 
    # It has now been rotated between 1 and n times. 
    # For example, the array nums = [1,2,3,4,5,6] might become:
    #    [3,4,5,6,1,2] if it was rotated 4 times.
    #    [1,2,3,4,5,6] if it was rotated 6 times.
    # Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.
    # A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

    # If the rotation count, r, is know, the minimum element is located at nums[r]
    # Since r is between 0 and nums.length, we can binary search possible all possible values of `r`
    #    this will take log(n) time
    # At each index, if we look at a pair of nums and nums[r] > nums[r + 1] then we know we found the rotation count
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        m = 0
        if len(nums) <= 2:
            return min(nums)
        if nums[left] < nums[right]:
            return nums[0]

        # Rotated array has 2 ascending sequeces, we need to find the location m
        # where nums[m] > nums[m+1] (all elements are unique)
        while not nums[m] > nums[m+1]:
            m = (right + left) // 2
            # If in the left ascending sequence, advance left
            if nums[0] < nums[m]:
                left = m + 1
            else: # If in right ascending sequece, reduce right
                right = m

        # Now that the loop is over, we know that nums[m] >= nums[m+1]
        return nums[m + 1]
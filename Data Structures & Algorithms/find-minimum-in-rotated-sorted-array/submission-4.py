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
        rc_lo = 0
        rc_hi = len(nums) - 1
        if len(nums) <= 2:
            return min(nums)
        if nums[rc_lo] < nums[rc_hi]:
            return nums[0]

        m = 0
        # Rotated array has 2 ascending sequeces, we need to find the location m
        # where nums[m] > nums[m+1] (all elements are unique)
        while nums[m] < nums[m+1]:
            m = (rc_hi + rc_lo) // 2
            print(rc_lo, rc_hi, m)
            # If in the left ascending sequence, advance rc_lo
            if nums[0] < nums[m]:
                rc_lo = m + 1
            else: # If in right ascending sequece, reduce rc_hi
                rc_hi = m
                
        # Now that the loop is over, we know that nums[m] >= nums[m+1]
        return nums[m + 1]
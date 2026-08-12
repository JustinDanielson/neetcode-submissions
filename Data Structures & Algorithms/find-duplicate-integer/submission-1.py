class Solution:
    # You are given an array of integers nums containing n + 1 integers. Each integer in nums is in the range [1, n] inclusive.
    # There is exactly one repeated integer in nums, and every other integer appears at most once.
    # Return the repeated integer.
    
    # The question text is pretty nuanced. The nums input array is length n and all digits are between[1,n] inclusive
    # So if the list is of length 10, you know that the numbers will all be between 1-10 with 1 number appearing
    # 2 or more times. This means not every number between 1-10 will be present. [1,2,3,4,5,6,7,8,8,8] is valid

    # Optimal solutions: Treat this as a linked list, instead of traversing it linearly, treat the number at each 
    # index as a .next pointer and go to that location in the list. Do this with a fast & slow pointer. You will eventually
    # be stuck in a loop and have both pointers equal in value.
    # This optimal solution is heavily predicated on the nuances of the input rules. Because there is no 0, you can't fall into a
    # loop of nums[0] -> 0. Because we're looking for the only dupe, if you have nums[2] == 2, then you would need a 2nd 2 to put you
    # into the trap of infinitely looping on 2. So you're guaranteed to have unique chains that always contain a loop.
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0,0
        # This guarantees that slow is in the loop
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # I'm not really sure how to prove that this loop works. slow2 needs to move
        # several times before it enters the loop. Then slow and slow2 are moving at the same speed.
        # slow and fast must meet at a special index that reflects the total length of the loop, or the distance
        # from 0 to loop start.
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

#    def findDuplicate(self, nums: List[int]) -> int:
#        dupeCheck = [0] * (len(nums)//32 + 1)
#        def _seen(num: int):
#            bitmask = 1 << (num % 32)
#            dupeCheck[num // 32] ^= bitmask
#            return (dupeCheck[num // 32] & bitmask) == 0
#        
#        for num in nums:
#            if _seen(num):
#                return num
#        
#        return -1
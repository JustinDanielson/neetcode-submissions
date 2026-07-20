class Solution:
    #Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
    #A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. 
    # The elements do not have to be consecutive in the original array.
    #You must write an algorithm that runs in O(n) time.
    #Constraints:
    #    0 <= nums.length <= 1000
    #    -10^9 <= nums[i] <= 10^9
    # Brute force is O(nlogn)
    # To eliminate sorting, I can use a hash table, each time I hash I check for key-1 and key+1,
    # if either are hits, then I keep doing +1, -1 to determine the length of this new sequence
    # store the best result if it is the new best
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        best_sequence_length = 0
        for num in nums:
            # if start of sequence
            if num - 1 not in seen:
                seq_len = 1
                while num + seq_len in seen:
                    seq_len += 1
                if seq_len > best_sequence_length:
                    best_sequence_length = seq_len
        return best_sequence_length
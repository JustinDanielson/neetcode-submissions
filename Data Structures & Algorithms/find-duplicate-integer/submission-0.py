class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dupeCheck = [0] * (10000//32 + 1)
        def _seen(num: int):
            bitmask = 1 << (num % 32)
            dupeCheck[num // 32] ^= bitmask
            return (dupeCheck[num // 32] & bitmask) == 0
        
        for num in nums:
            if _seen(num):
                return num
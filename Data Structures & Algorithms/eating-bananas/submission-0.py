from math import ceil
class Solution:
    # Koko the monkey has an array of piles of bananas
    # Koko can spend 1 hour at each pile when they visit it, even if all the bananas are consumed
    # Find the lowest bananas consumed per hour, k, such that Koko spends the most hours eating
    # without going over the time limit of h (in hours).
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = 1000000000
        # Since k must be between [1,1billion], we can binary search all possibilities of k
        # binary search brute force k with l and r set to 1, 1bn
        while l < r:
            k = (l + r) // 2
            total_hours_eating = sum(map(lambda num: ceil(num / k), piles))
            # if koko ate too fast, eat more slowly, so lower `r`
            if total_hours_eating <= h:
                r = k
            # if koko ate too slow, eat faster, so increase `l`
            elif total_hours_eating > h:
                l = k + 1
        
        return r
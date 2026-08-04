class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == 1:
            return math.ceil(piles[0] / h)

        l = math.ceil(sum(piles) / h)
        max_avg_time_per_pile = h // len(piles)
        r = math.ceil(max(piles) / max_avg_time_per_pile)
        min_k = r
        while l <= r:
            m = l + ((r-l) // 2)
            time_needed = 0
            for pile in piles:
                time_needed += math.ceil(pile / m)
            
            if time_needed <= h:
                min_k = m
                r = m-1
            else:
                l = m+1
        
        return min_k
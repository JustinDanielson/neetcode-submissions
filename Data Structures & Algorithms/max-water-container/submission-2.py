class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = heights.index(max(heights))
        r = l
        best = [l, r]
        best_volume = min([heights[l], heights[r]]) * (r - l)
        # With l being the tallest bar, find the best r
        while r != len(heights):
            volume = min(heights[l], heights[r]) * (r - l)
            if volume >= best_volume:
                best = [l, r]
                best_volume = volume
                print("New best")
                print(best_volume)
            r += 1
        l, r = best
        # With r being the best bar, find the best l
        while l >= 0:
            volume = min([heights[l], heights[r]]) * (r - l)
            if volume >= best_volume:
                best = [l, r]
                best_volume = volume
            l -= 1
        return best_volume
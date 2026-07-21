class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = heights.index(max(heights))
        r = l
        best_volume = min([heights[l], heights[r]]) * (r - l)
        # With l being the tallest bar, find the best r
        for i in range(r + 1, len(heights)):
            volume = min(heights[l], heights[i]) * (i - l)
            if volume >= best_volume:
                best_volume = volume
                r = i
        # With r being the best bar, find the best l
        for i in reversed(range(0, l)):
            volume = min([heights[i], heights[r]]) * (r - i)
            if volume >= best_volume:
                best_volume = volume
                l = i
        return best_volume
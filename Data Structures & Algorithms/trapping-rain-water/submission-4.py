class Solution:
    # You are given an array of non-negative integers `height` which represent an elevation map.
    # Each value `height[i]` represents the height of a bar, which has a width of 1.
    # Return the maximum area of water taht can be trapped between all the bars.
    # First go left to right looking for containers where the right bar is >= left height
    # Then go right to left looking for containers where the left bar is > the right bar height
    def trap(self, height: List[int]) -> int:
        l , r = 0, 1
        total = 0
        # This finds all containers where the right wall is taller or equal to the left
        while r < len(height):
            if height[r] < height[l]:
                r += 1
            elif height[r] >= height[l] and r - l <= 1:
                l += 1
                r += 1
            elif height[r] >= height[l] and r - l > 1:
                short_height = min([height[r], height[l]])
                total += sum([short_height - height[i] for i in range(l + 1, r)])
                l = r
                r += 1
        # Now find all containers where the left wall is taller than the right
        r = len(height) - 1
        l = r - 1
        while l >= 0:
            if height[l] <= height[r]:
                l -= 1
            elif height[l] >= height[r] and r - l <= 1:
                l -= 1
                r -= 1
            elif height[l] > height[r] and r - l > 1:
                short_height = min([height[r], height[l]])
                total += sum([short_height - height[i] for i in range(l + 1, r)])
                r = l
                l -= 1
        return total
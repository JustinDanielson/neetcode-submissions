class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Monotonic increasing stack
        # Store the height and the index where that height was found
        bars = []
        best_box = [0,0] #w,h
        for i,h in enumerate(heights):
            new_bar_leftmost_pos = i
            while bars and h <= bars[-1][0]:
                left_bar = bars.pop()
                # newest bar will take position of bars popped from stack
                # to account for leftwards expansion of it's rectangle
                # ex: 4,3,2 should be h=2,w=3
                new_bar_leftmost_pos = left_bar[1]
                height, width = left_bar[0], i - left_bar[1]
                area = height * width
                if area > best_box[0] * best_box[1]:
                    best_box = [height, width]
            # all of the bars popped off are taller than `h`, so set pos
            # to just after any prior shorter bar. 0 if there are none
            # pos = 0 if not bars else bars[-1][1] + 1
            bars.append([h, new_bar_leftmost_pos])
        # the remaining bars that come after them, extend their widths from
        # their position to the end of the histogram
        while bars:
            left_bar = bars.pop()
            h = left_bar[0]
            w = len(heights) - left_bar[1]
            area = w * h
            if area > best_box[0] * best_box[1]:
                best_box = [h, w]
        return best_box[0] * best_box[1]
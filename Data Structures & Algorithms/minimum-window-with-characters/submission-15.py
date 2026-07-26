from collections import defaultdict
class Solution:
    # This method checks to see if the str t has all characters in the substr that is the window
    def _is_valid_window(self, t_frequency: defaultdict, window_frequency: defaultdict):
        # all character in t_frequency exists as many or fewer times as in the window
        return all([t_frequency[c] <= window_frequency[c] for c in t_frequency.keys()])

    def minWindow(self, s: str, t: str) -> str:
        res = s
        frame = list()
        window_start = 0
        window_end = len(s) - 1
        tFreq = defaultdict(int) #t parm freq
        wFreq = defaultdict(int) #window freq

        for c in t:
            tFreq[c] += 1
        for c in s:
            wFreq[c] += 1

        if len(t) > len(s) or not self._is_valid_window(tFreq, wFreq):
            return ""

        window_start = 0
        while window_start <= len(s) - len(t):
            wFreq.clear()
            for window_end in range(window_start, len(s)):
                wFreq[s[window_end]] += 1
                # If new valid window found
                if s[window_end] in tFreq and self._is_valid_window(tFreq, wFreq):
                    if len(res) > window_end - window_start:
                        res = s[window_start: window_end + 1]
                # If this window exceeds the current res, break
                # # micro-optimization, commenting out
                # if window_end - window_start > len(res):
                #     break
            window_start += 1
        return res
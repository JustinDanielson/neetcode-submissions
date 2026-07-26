from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = [0, 0]
        resLen = len(s) + 1
        start = end = 0
        if len(t) > len(s):
            return ""
        
        tFreq = defaultdict(int)
        for c in t:
            tFreq[c] += 1

        wFreq = defaultdict(int)        
        match_count = 0
        for start in range(len(s) - len(t) + 1):
            # if window starts with char not in t, skip it
            if s[start] not in tFreq:
                continue
            
            if match_count < len(tFreq):
                # Given start, find a window between start to end that contains
                # all chars of t frequency
                end = start
                while match_count < len(tFreq) and end < len(s):
                    current_char = s[end]
                    if current_char in tFreq:
                        wFreq[current_char] += 1
                        if wFreq[current_char] == tFreq[current_char]:
                            match_count += 1
                    end += 1
            
            if wFreq[s[start]] > tFreq[s[start]]:
                # Shrink current valid substr from left side to look for minmal
                wFreq[s[start]] -= 1
            elif match_count == len(tFreq) and wFreq[s[start]] == tFreq[s[start]]:
                # No longer possible to shrink left side of window
                # this is a relative minimal substr where all chars are t are present
                if end - start < resLen:
                    # if the length is less than previous result, use this
                    res = [start, end]
                    resLen = end - start
                # reset state to look for other substrs
                wFreq.clear()
                match_count = 0
        return s[res[0]: res[1]]
from collections import defaultdict
class Solution:
    '''
    You are given a string s consisting of only uppercase english characters and an integer k.
    You can choose up to k characters of the string and replace them with any other uppercase English character.
    After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

    Sliding window implementation. A window is valid if the following condition is true. w - maxF <= k,
      where w is window width, maxF is the count of the most frequently occuring character in the window, and k is number of edits remaining
    
    The window will start with l = r = 0. If the window is valid, increase the width (r++). If the window is invalid, shift it (l++)
    '''
    def characterReplacement(self, s: str, k: int):
        res = 0
        freq = defaultdict(int)
        l = r = 0
        while r < len(s):
            freq[s[r]] += 1
            maxF = max(freq.items(), key=lambda item: item[1])[1]
            if (r - l + 1) - maxF > k: #window invalid
                l += 1
                freq[s[l - 1]] -= 1 #lower freq of char evicted from window
            else:
                res = r - l + 1
            r += 1
        return res
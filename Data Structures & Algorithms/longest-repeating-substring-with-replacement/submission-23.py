class Solution:
    '''
    You are given a string s consisting of only uppercase english characters and an integer k.
    You can choose up to k characters of the string and replace them with any other uppercase English character.
    After performing at most k replacements, return the length of the longest substring which contains only one distinct character.
    '''
    def characterReplacement(self, s: str, k: int):
        res = 0
        current_idx = 0
        l = 0
        while current_idx < len(s) - 1:
            # Ensure that we're only testing for characters that are unique relative to their left neighbor
            # Skip if this idx is part of a previously tested sequence
            if current_idx > 0 and s[current_idx] == s[current_idx - 1]:
                current_idx += 1
                continue

            # Set up left and right pointers
            l = current_idx
            r = current_idx + 1
            temp_k = k
            # Advance the right pointer until end of string or until k edits used
            while r < len(s) and (s[l] == s[r] or temp_k > 0):
                if s[l] != s[r]:
                    temp_k -= 1
                r += 1
            # If edits remaining, use them to expand left
            # Leftward expansion does not contain matching chars because previous iterations of the loop
            #    would have already tested for them.
            left_expansion = min([temp_k, l])
            res = max([res, r - l + left_expansion])
            current_idx = l + 1
        return res
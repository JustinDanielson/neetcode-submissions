class Solution:
    '''
    You are given a string s consisting of only uppercase english characters and an integer k.
    You can choose up to k characters of the string and replace them with any other uppercase English character.
    After performing at most k replacements, return the length of the longest substring which contains only one distinct character.
    '''
    def characterReplacement(self, s: str, k: int):
        res = 0
        current_idx = 0
        l, r = 0, 0
        while current_idx < len(s) - 1:
            # Skip if this idx is part of a previously tested sequence
            if current_idx > 0 and s[current_idx] == s[current_idx - 1]:
                current_idx += 1
                r += 1
                continue

            l = current_idx
            temp_k = k
            while r < len(s) and (s[l] == s[r] or temp_k > 0):
                if s[l] != s[r]:
                    temp_k -= 1
                r += 1
            print(l, r)
            left_expansion = min([temp_k, l])
            res = max([res, r - l + left_expansion])
            current_idx = l + 1
            r = current_idx + 1
        return res
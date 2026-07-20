class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean str, remove all non-alpha and normalize casing
        clean_str = list([ch for ch in s.lower() \
            if ch.isalnum()])
        l,r = 0, len(clean_str) - 1
        while l < r and clean_str[l] == clean_str[r]:
            l += 1
            r -= 1
        # if l < r is false, then all l/r pairs are equal
        return not l < r
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        res = 1
        seen = set()
        l, r = 0, 1
        seen.add(s[0])
        while r < len(s):
            if s[r] in seen:
                l += 1
                r = l
                seen.clear()
                seen.add(s[l])
            else:
                seen.add(s[r])
                res = max([res, len(seen)])
            r += 1
        return res

        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = sorted(list(s.lower()))
        t_chars = sorted(list(t.lower()))
        return s_chars == t_chars
        
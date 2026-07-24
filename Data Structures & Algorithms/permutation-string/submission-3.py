class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = r = 0
        while l <= len(s2) - len(s1):
            chars = list(s1)
            r = l
            while len(chars) > 0 and s2[r] in chars:
                chars.remove(s2[r])
                r += 1
            if len(chars) == 0:
                return True
            else:
                l += 1
        return False

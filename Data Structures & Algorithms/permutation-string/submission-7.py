from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = r = 0
        s1counts = [0]*26
        s2counts = [0]*26
        for c in s1:
            s1counts[ord(c) - ord('a')] += 1
        while l <= len(s2) - len(s1):
            r = l
            i = 0
            for i in range(len(s1)):
                ch = ord(s2[l + i]) - ord('a') #get char in potential anagram
                s2counts[ch] += 1 #count it
                if s2counts[ch] > s1counts[ch]: #if not valid permutation of s1
                    l += 1
                    break
            if s2counts == s1counts:
                return True
            else:
                for j in range(26):
                    s2counts[j] = 0
        return False

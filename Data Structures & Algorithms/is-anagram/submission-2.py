class Solution:
    # # Brute force
    # def isAnagram(self, s: str, t: str) -> bool:
    #     s_chars = sorted(list(s.lower()))
    #     t_chars = sorted(list(t.lower()))
    #     return s_chars == t_chars

    # Frequency Counting
    # If the strings are anagrams, counting the characters and substracting characters will result in all 0s
    def isAnagram(self, s: str, t: str) -> bool:
        counts: dict[str, int] = dict()
        for c in s.lower():
            counts[c] = counts.get(c,0) + 1
        for c in t.lower():
            counts[c] = counts.get(c,0) - 1
        return all(value == 0 for value in counts.values())
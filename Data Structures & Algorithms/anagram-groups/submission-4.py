class Solution:
    # O(nlogn)
    def str_to_key_Onlogn(self, s: str) -> str:
        return "".join(sorted(list(s.lower())))

    # O(n)
    def str_to_key_On(self, s: str) -> List[int]:
        counts = [0]*26
        for ch in s:
            counts[ord(ch) - ord('a')] += 1
        return tuple(counts)


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        key_method = self.str_to_key_Onlogn
        seq_map: dict[Any,int] = dict()
        unique_seq_count = 0
        results = list()
        for s in strs:
            seq = key_method(s)
            # Create result list if this seq is new
            if seq not in seq_map:
                seq_map[seq] = unique_seq_count
                unique_seq_count += 1
                results.append([])
            results[seq_map[seq]].append(s)
        return results
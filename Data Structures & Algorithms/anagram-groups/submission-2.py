class Solution:
    def str_to_key(self, s: str):
        return "".join(sorted(list(s.lower())))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seq_map: dict[str,int] = dict()
        unique_seq_count = 0
        results = list()
        for s in strs:
            seq = self.str_to_key(s)
            # Create result list if this seq is new
            if seq not in seq_map:
                seq_map[seq] = unique_seq_count
                unique_seq_count += 1
                results.append([])
            results[seq_map[seq]].append(s)
        return results
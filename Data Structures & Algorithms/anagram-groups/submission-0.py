class Solution:
    # Brute force
    # Sort each str's characters
    # If sorted chr sequence is new, hash it with count++
    # Do this for all strs and store them into List[List[str]]
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seq_map: dict[str,int] = dict()
        unique_seq_count = 0
        results = list()
        for s in strs:
            seq = "".join(sorted(list(s.lower())))
            # Create result list if this seq is new
            if seq not in seq_map:
                seq_map[seq] = unique_seq_count
                unique_seq_count += 1
                results.append([])
            results[seq_map[seq]].append(s)
        return results
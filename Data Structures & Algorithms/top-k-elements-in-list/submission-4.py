from collections import defaultdict
class Solution:
    # In the list nums, return the k most frequently occuring numbers
    # select num, count(*) from nums group by num order by count(*) desc limit k;
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        # Count the frequency of each number {num: count}
        for num in nums:
            frequency[num] += 1
        # Sort by frequency descending and return the top k
        # Create list of top k occuring numbers (item[0])
        return [item[0] for item in 
                sorted(frequency.items(), key=lambda item: item[1], reverse=True)[:k]
        ]
        
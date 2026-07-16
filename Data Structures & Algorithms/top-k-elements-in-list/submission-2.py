from collections import defaultdict
class Solution:
    # In the list nums, return the k most frequently occuring numbers
    # select num, count(*) from nums group by num order by count(*) desc limit k;
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        for num in nums:
            frequency[num] += 1
        return [item[0] for item in 
                sorted(frequency.items(), key=lambda item: item[1], reverse=True)[:k]
        ]
        
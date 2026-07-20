from collections import defaultdict
class Solution:
    # In the list nums, return the k most frequently occuring numbers
    # select num, count(*) from nums group by num order by count(*) desc limit k;
    # Brute Force: this is n * nlogn
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     frequency = defaultdict(int)
    #     # Count the frequency of each number {num: count}
    #     for num in nums:
    #         frequency[num] += 1
    #     # Sort by frequency descending and return the top k
    #     # Create list of top k occuring numbers (item[0])
    #     return [item[0] for item in 
    #             sorted(frequency.items(), key=lambda item: item[1], reverse=True)[:k]
    #     ]

    # Bucket Sort the frequencies
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        # Count the frequency of each number {num: count} O(n)
        for num in nums:
            frequency[num] += 1
        
        # Store numbers in their frequency buckets O(n)
        freq_buckets = [[] for _ in range(len(nums))]
        for num,freq in frequency.items():
            # 1-based array bc frequency 0 is invalid (v - 1)
            freq_buckets[freq - 1].append(num)
        
        # Create result list traversing backwards
        results = list()
        for numbers in reversed(freq_buckets):
            if len(results) < k and numbers != []:
                results += numbers
        return results
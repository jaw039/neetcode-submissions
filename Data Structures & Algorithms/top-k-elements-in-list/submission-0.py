class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for item in nums:
            freq[item] += 1
        
        sorted_items = sorted(freq.items(), key = lambda item: item[1], reverse= True)
        return [pair[0] for pair in sorted_items[:k]]



        

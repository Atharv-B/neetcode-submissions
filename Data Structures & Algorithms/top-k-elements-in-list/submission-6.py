class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 0
            freq[i] += 1
        print(freq)
        sorted_d = sorted(freq, key=freq.get, reverse=True)
        return sorted_d[:k]
        
        
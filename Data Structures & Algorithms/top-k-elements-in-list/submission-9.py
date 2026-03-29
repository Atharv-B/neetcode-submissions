class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_counter = {}
        for i in range(len(nums)):
            if nums[i] not in freq_counter:
                freq_counter[nums[i]] = 1
            else:
                freq_counter[nums[i]] += 1
        print(freq_counter)
        freq_counter_sorted = sorted(freq_counter, key=freq_counter.get,reverse=True)
        print(freq_counter_sorted)
        return freq_counter_sorted[:k]
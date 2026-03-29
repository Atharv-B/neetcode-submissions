class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        frequency = {}
        for item in nums:
            if item in frequency:
                return True
            else:
                frequency[item] = 1

        return False
        
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0

        for i in nums:
            if i-1 not in nums:
                curr_long = 0
                while (i+curr_long) in nums:
                    curr_long += 1
                    longest = max(longest, curr_long)
        return longest

        
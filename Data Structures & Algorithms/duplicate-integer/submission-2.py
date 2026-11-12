class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_dupes = set()
        for i in nums:
            if i in has_dupes:
                return True
            has_dupes.add(i)
        return False
        
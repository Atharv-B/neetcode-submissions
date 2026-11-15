class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Example [1,2,3,4,5], target = 4
        # mid = 3
        # if target > mid then move left pointer to mid.
        # if target < mid then move right pointer to mid
        # else if mid == target then return index.
        left = 0
        right = len(nums) - 1

        while left<=right:
            mid = (left+right)//2
            if target > nums[mid]:
                left = mid+1
            elif target < nums[mid]:
                right = mid-1
            elif nums[mid]==target:
                return mid
        return -1



        
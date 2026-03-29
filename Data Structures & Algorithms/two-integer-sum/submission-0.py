class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Sol 1
        hmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hmap:
                return [hmap[complement], i]
            hmap[nums[i]] = i
        # Sol 2
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i] + nums[j+1] == target:
        #             return [i, j+1]
        # return []


            

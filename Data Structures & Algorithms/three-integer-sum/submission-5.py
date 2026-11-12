class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        output = []
        for i in range(len(nums)):
            if nums[i] == nums[i-1] and i>0:
                continue
            left = i+1
            right = len(nums) - 1
            while left<right:
                target = nums[i] + nums[left] + nums[right]

                if target > 0:
                    right-=1
                if target < 0:
                    left+=1
                if target == 0:
                    output.append([nums[i], nums[left], nums[right]])
                    left+=1 
                    while nums[left] == nums[left-1] and left< right:
                        left+=1
        return output


        
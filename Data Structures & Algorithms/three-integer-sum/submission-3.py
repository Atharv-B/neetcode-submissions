class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        output = []

        for i in range(len(nums)):
            if nums[i] == nums[i-1] and i>0:
                continue
            left = i+1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                # print(total)
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    output.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left<right:
                        left+=1
                    
        return output
        
        
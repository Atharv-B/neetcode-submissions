class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ele_right = [1] * len(nums)
        ele_left =  [1] * len(nums)
        for i in range(1, len(nums)):
            ele_right[i] = ele_right[i-1]*nums[i-1]
        print(ele_right)
        for i in range(len(nums)-2, -1, -1):
            ele_left[i] = ele_left[i+1]*nums[i+1]
        print(ele_left)
        output = [None] * len(nums)
        for i in range(len(nums)):
            output[i] = ele_right[i]*ele_left[i]
        return output



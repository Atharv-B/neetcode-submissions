class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [] 
        postfix = []
        output = []
        prefix_curr = 1
        postfix_curr = 1
        res = 0

        for i in range(len(nums)):
            prefix_curr *= nums[i]
            prefix.append(prefix_curr)
        # print(prefix)

        for j in nums[::-1]:
            postfix_curr *= j
            postfix.append(postfix_curr)
        postfix = postfix[::-1]
        # print(postfix)

        for k in range(len(nums)):
            if k == 0:
                output.append(1*postfix[k+1])
            elif k == len(nums) - 1:
                output.append(1*prefix[k-1])
            else:
                output.append(prefix[k-1]*postfix[k+1])
    
        return output



            
        


        
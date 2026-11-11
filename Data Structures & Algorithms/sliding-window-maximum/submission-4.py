import collections
# if the num < what you are adding to queue, you are allowed to do it.
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()
        left = right = 0

        for i in range(len(nums)):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)

            if left > q[0]:
                q.popleft()

            if (right+1)>=k:
                output.append(nums[q[0]])
                left += 1

            right+=1
        return output

            
        

             
        
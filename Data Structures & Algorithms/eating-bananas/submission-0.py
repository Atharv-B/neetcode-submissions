class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # for the give example input - [1,4,3,2], h(time_limit) = 9
        # for k = 
        # time required for piles[i] = [1,2,2,1] = 6 < 9
        left = 1
        right = max(piles)
        lowest = 9999999999

        while left <= right:
            mid = (left+right)//2
            total_time = 0
            for i in piles:
                import math
                total_time += math.ceil(i/mid) 

            if total_time>h:
                left = mid + 1
            elif total_time<=h:
                
                lowest = min(lowest, mid)
                right = mid -1
        return lowest
            
                
        


        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        res = 0
        while left < right and right < len(prices):
            if prices[left] > prices[right]:
                left = right
            else:
                profit = prices[right] - prices[left]
                res = max(profit, res)
                
            right+=1
        return res
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        profit = 0
        window = []
        while left <= right and right < len(prices):
            if prices[left] < prices[right]:
                gain = prices[right] - prices[left]
                profit = max(gain, profit)
            else:
                left= right
            right +=1
        return profit
            

            




        
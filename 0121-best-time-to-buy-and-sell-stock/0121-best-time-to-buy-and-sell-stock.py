class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_val:
                min_val = price
            if price - min_val > max_profit:
                max_profit = price - min_val
        
        return max_profit
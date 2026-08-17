class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = 101
        max_profit = 0
        for i in range(1, len(prices)):
            min_so_far = min(min_so_far, prices[i - 1])
            max_profit = max(max_profit, prices[i] - min_so_far)
        
        return max(0, max_profit)


        
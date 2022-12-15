from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        profit = 0
        for num in prices:
            lowest = min(lowest, num)
            profit = max(profit, num - lowest)
        return profit
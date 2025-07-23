class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_ = float('inf')
        max_profit = 0

        for p in prices:
            if p < min_:
                min_ = p
            else: max_profit = max(max_profit, p - min_)
        
        return max_profit
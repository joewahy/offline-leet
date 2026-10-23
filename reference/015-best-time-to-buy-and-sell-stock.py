class Solution:
    def maxProfit(self, prices):
        low, best = prices[0], 0
        for p in prices:
            low = min(low, p)
            best = max(best, p - low)
        return best

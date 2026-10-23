class Solution:
    def maxCoins(self, nums):
        a = [1] + nums + [1]
        n = len(a)
        dp = [[0] * n for _ in range(n)]
        for length in range(2, n):
            for lo in range(n - length):
                hi = lo + length
                dp[lo][hi] = max(dp[lo][k] + dp[k][hi] + a[lo] * a[k] * a[hi] for k in range(lo + 1, hi))
        return dp[0][n - 1]

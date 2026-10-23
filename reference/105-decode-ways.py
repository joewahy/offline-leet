class Solution:
    def numDecodings(self, s):
        n = len(s)
        dp = [0] * n + [1]
        for i in range(n - 1, -1, -1):
            if s[i] != "0":
                dp[i] = dp[i + 1]
                if i + 1 < n and s[i:i + 2] <= "26":
                    dp[i] += dp[i + 2]
        return dp[0]

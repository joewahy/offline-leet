class Solution:
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [False] * (len(s2) + 1)
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i == 0 and j == 0:
                    dp[j] = True
                    continue
                ok = False
                if i and dp[j] and s1[i - 1] == s3[i + j - 1]:
                    ok = True
                if j and dp[j - 1] and s2[j - 1] == s3[i + j - 1]:
                    ok = True
                dp[j] = ok
        return dp[len(s2)]

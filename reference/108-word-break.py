class Solution:
    def wordBreak(self, s, wordDict):
        words = set(wordDict)
        longest = max(map(len, words))
        can = [True] + [False] * len(s)
        for i in range(1, len(s) + 1):
            for j in range(max(0, i - longest), i):
                if can[j] and s[j:i] in words:
                    can[i] = True
                    break
        return can[-1]

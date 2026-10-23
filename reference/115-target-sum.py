from collections import Counter


class Solution:
    def findTargetSumWays(self, nums, target):
        ways = Counter({0: 1})
        for x in nums:
            nxt = Counter()
            for total, count in ways.items():
                nxt[total + x] += count
                nxt[total - x] += count
            ways = nxt
        return ways[target]

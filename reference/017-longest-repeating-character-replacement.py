from collections import defaultdict


class Solution:
    def characterReplacement(self, s, k):
        count = defaultdict(int)
        left = best = 0
        for right, ch in enumerate(s):
            count[ch] += 1
            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            best = max(best, right - left + 1)
        return best

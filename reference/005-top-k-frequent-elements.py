from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        return [n for n, _ in Counter(nums).most_common(k)]

from collections import Counter


class Solution:
    def leastInterval(self, tasks, n):
        counts = Counter(tasks)
        top = max(counts.values())
        ties = sum(1 for c in counts.values() if c == top)
        return max(len(tasks), (top - 1) * (n + 1) + ties)

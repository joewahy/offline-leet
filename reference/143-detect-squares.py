from collections import Counter


class DetectSquares:
    def __init__(self):
        self.counts = Counter()

    def add(self, point):
        self.counts[tuple(point)] += 1

    def count(self, point):
        x, y = point
        total = 0
        for (px, py), c in list(self.counts.items()):
            if abs(px - x) == abs(py - y) and px != x:
                total += c * self.counts[(px, y)] * self.counts[(x, py)]
        return total

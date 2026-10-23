class Solution:
    def mergeTriplets(self, triplets, target):
        got = [0, 0, 0]
        for t in triplets:
            if all(a <= b for a, b in zip(t, target)):
                got = [max(a, b) for a, b in zip(got, t)]
        return got == target

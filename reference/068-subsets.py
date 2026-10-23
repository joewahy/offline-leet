class Solution:
    def subsets(self, nums):
        out = [[]]
        for x in nums:
            out += [s + [x] for s in out]
        return out

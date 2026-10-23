class Solution:
    def missingNumber(self, nums):
        out = len(nums)
        for i, x in enumerate(nums):
            out ^= i ^ x
        return out

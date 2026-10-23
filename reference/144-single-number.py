class Solution:
    def singleNumber(self, nums):
        out = 0
        for x in nums:
            out ^= x
        return out

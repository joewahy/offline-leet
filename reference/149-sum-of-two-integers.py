class Solution:
    def getSum(self, a, b):
        mask, biggest = 0xFFFFFFFF, 0x7FFFFFFF
        a, b = a & mask, b & mask
        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        return a if a <= biggest else ~(a ^ mask)

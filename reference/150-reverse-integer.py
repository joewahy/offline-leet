class Solution:
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0
        while x:
            x, digit = divmod(x, 10)
            rev = rev * 10 + digit
        rev *= sign
        return rev if -(2 ** 31) <= rev <= 2 ** 31 - 1 else 0

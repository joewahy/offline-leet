from spec import P

CATEGORY = "bit-manipulation"


def _ints(rng, n, lo, hi):
    return [rng.randint(lo, hi) for _ in range(n)]


def _single(rng, pairs, lo=-50, hi=50):
    vals = rng.sample(range(lo, hi + 1), pairs + 1)
    nums = vals[:1] + vals[1:] * 2
    rng.shuffle(nums)
    return [nums]


def _missing(rng, n):
    nums = list(range(n + 1))
    nums.remove(rng.randint(0, n))
    rng.shuffle(nums)
    return [nums]


PROBLEMS = [
    P(144, "Single Number", "Easy", "singleNumber",
      r'''
In the list `nums`, every integer appears exactly twice except for one integer that appears once. Return the integer that appears once.

Use O(n) time and O(1) extra space.

## Examples

```
Input:  nums = [3, 2, 3]
Output: 2

Input:  nums = [7, 6, 6, 7, 8]
Output: 8
```

## Constraints

- `1 <= len(nums) <= 9999` (always odd)
- `-30000 <= nums[i] <= 30000`

## Hints

- XOR of a number with itself is `0`, and XOR with `0` leaves a number unchanged. XOR everything together.
''',
      r'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        pass
''',
      r'''
class Solution:
    def singleNumber(self, nums):
        out = 0
        for x in nums:
            out ^= x
        return out
''',
      [([[3, 2, 3]], 2), ([[7, 6, 6, 7, 8]], 8), ([[1]], 1), ([[4, 1, 2, 1, 2]], 4), ([[-1, -1, -2]], -2),
       ([[0, 1, 0]], 1), ([[2, 2, 1]], 1)],
      gen=lambda rng: [_single(rng, p) for p in (1, 3, 8, 20)] + [_single(rng, 4999, -30000, 30000)],
      small=lambda rng: _single(rng, rng.randint(0, 6)),
      brute=r'''
from collections import Counter


class Solution:
    def singleNumber(self, nums):
        return next(k for k, v in Counter(nums).items() if v == 1)
'''),

    P(145, "Number of 1 Bits", "Easy", "hammingWeight",
      r'''
Given a positive integer `n`, return the number of `1` bits in its binary representation (also called its Hamming weight).

## Examples

```
Input:  n = 11
Output: 3          # 1011

Input:  n = 128
Output: 1
```

## Constraints

- `1 <= n <= 2^31 - 1`

## Hints

- `n & (n - 1)` clears the lowest set bit. Count how many times you can do it before `n` becomes `0`.
''',
      r'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        pass
''',
      r'''
class Solution:
    def hammingWeight(self, n):
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count
''',
      [([11], 3), ([128], 1), ([2147483645], 30), ([1], 1), ([255], 8), ([2147483647], 31), ([8], 1), ([1023], 10)],
      gen=lambda rng: [[rng.randint(1, 100)] for _ in range(4)] + [[rng.randint(1, 2 ** 31 - 1)] for _ in range(4)] + [[2 ** 30], [2 ** 31 - 2]],
      small=lambda rng: [rng.randint(1, 5000)],
      brute=r'''
class Solution:
    def hammingWeight(self, n):
        return bin(n).count("1")
'''),

    P(146, "Counting Bits", "Easy", "countBits",
      r'''
Given an integer `n`, return a list `ans` of length `n + 1` where `ans[i]` is the number of `1` bits in the binary representation of `i`.

Aim for O(n) time total, by reusing results you already computed.

## Examples

```
Input:  n = 4
Output: [0, 1, 1, 2, 1]

Input:  n = 2
Output: [0, 1, 1]
```

## Constraints

- `0 <= n <= 10000`

## Hints

- `i` has the same bits as `i >> 1` plus possibly one more (its lowest bit).
''',
      r'''
class Solution:
    def countBits(self, n: int) -> List[int]:
        pass
''',
      r'''
class Solution:
    def countBits(self, n):
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans
''',
      [([4], [0, 1, 1, 2, 1]), ([2], [0, 1, 1]), ([0], [0]), ([1], [0, 1]), ([5], [0, 1, 1, 2, 1, 2]),
       ([8], [0, 1, 1, 2, 1, 2, 2, 3, 1])],
      gen=lambda rng: [[n] for n in (3, 16, 31, 100, 1000, 10000)],
      small=lambda rng: [rng.randint(0, 40)],
      brute=r'''
class Solution:
    def countBits(self, n):
        return [bin(i).count("1") for i in range(n + 1)]
'''),

    P(147, "Reverse Bits", "Easy", "reverseBits",
      r'''
Given an unsigned 32-bit integer `n`, reverse its bits (treat it as exactly 32 binary digits) and return the resulting unsigned integer.

## Examples

```
Input:  n = 3          # 00000000000000000000000000000011
Output: 3221225472     # 11000000000000000000000000000000

Input:  n = 43261596
Output: 964176192
```

## Constraints

- `0 <= n <= 2^32 - 1`

## Hints

- Build the answer one bit at a time: shift the result left, then add the lowest bit of `n`, then shift `n` right. Do this 32 times.
''',
      r'''
class Solution:
    def reverseBits(self, n: int) -> int:
        pass
''',
      r'''
class Solution:
    def reverseBits(self, n):
        out = 0
        for _ in range(32):
            out = (out << 1) | (n & 1)
            n >>= 1
        return out
''',
      [([43261596], 964176192), ([2147483648], 1), ([1], 2147483648), ([0], 0), ([4294967295], 4294967295),
       ([3], 3221225472), ([5], 2684354560)],
      gen=lambda rng: [[rng.randint(0, 2 ** 32 - 1)] for _ in range(6)] + [[2 ** 16], [255], [2 ** 32 - 2]],
      small=lambda rng: [rng.randint(0, 2 ** 32 - 1)],
      brute=r'''
class Solution:
    def reverseBits(self, n):
        return int(format(n, "032b")[::-1], 2)
'''),

    P(148, "Missing Number", "Easy", "missingNumber",
      r'''
`nums` contains `n` distinct integers taken from the range `[0, n]`, so exactly one number from that range is missing. Return it.

## Examples

```
Input:  nums = [1, 2, 3]
Output: 0

Input:  nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
Output: 8
```

## Constraints

- `1 <= n <= 10000`
- All numbers are distinct and between `0` and `n`.

## Hints

- The sum `0 + 1 + ... + n` is known. Or XOR every index and every value together.
''',
      r'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        pass
''',
      r'''
class Solution:
    def missingNumber(self, nums):
        out = len(nums)
        for i, x in enumerate(nums):
            out ^= i ^ x
        return out
''',
      [([[1, 2, 3]], 0), ([[0, 1]], 2), ([[0]], 1), ([[1]], 0), ([[3, 0, 1]], 2), ([[9, 6, 4, 2, 3, 5, 7, 0, 1]], 8),
       ([[0, 1, 2, 3]], 4), ([[4, 2, 1, 0]], 3)],
      gen=lambda rng: [_missing(rng, n) for n in (2, 5, 12, 40)] + [_missing(rng, 10000)],
      small=lambda rng: _missing(rng, rng.randint(1, 10)),
      brute=r'''
class Solution:
    def missingNumber(self, nums):
        return next(i for i in range(len(nums) + 1) if i not in nums)
'''),

    P(149, "Sum of Two Integers", "Medium", "getSum",
      r'''
Return the sum of two integers `a` and `b` without using the operators `+` and `-`.

(The tests cannot enforce this rule, but the point of the problem is to build addition out of bit operations.)

## Examples

```
Input:  a = 1, b = 2
Output: 3

Input:  a = -2, b = -3
Output: -5
```

## Constraints

- `-1000 <= a, b <= 1000`

## Hints

- `a ^ b` adds without carrying, and `(a & b) << 1` is the carry. Repeat until there is no carry.
- In Python, integers are unbounded, so mask to 32 bits and convert back to a signed value at the end.
''',
      r'''
class Solution:
    def getSum(self, a: int, b: int) -> int:
        pass
''',
      r'''
class Solution:
    def getSum(self, a, b):
        mask, biggest = 0xFFFFFFFF, 0x7FFFFFFF
        a, b = a & mask, b & mask
        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        return a if a <= biggest else ~(a ^ mask)
''',
      [([1, 2], 3), ([2, 3], 5), ([-1, 1], 0), ([-2, -3], -5), ([0, 0], 0), ([20, 30], 50), ([-5, 10], 5),
       ([1000, -1000], 0), ([-1000, -1000], -2000), ([123, 456], 579)],
      gen=lambda rng: [[rng.randint(-1000, 1000), rng.randint(-1000, 1000)] for _ in range(10)] + [[1000, 1000], [-1000, 1000], [7, -7]],
      small=lambda rng: [rng.randint(-60, 60), rng.randint(-60, 60)],
      brute=r'''
class Solution:
    def getSum(self, a, b):
        return a + b
'''),

    P(150, "Reverse Integer", "Medium", "reverse",
      r'''
Given a signed 32-bit integer `x`, return `x` with its decimal digits reversed (keeping the sign). If the reversed value does not fit in a signed 32-bit integer (outside `[-2^31, 2^31 - 1]`), return `0`.

## Examples

```
Input:  x = 123
Output: 321

Input:  x = -123
Output: -321

Input:  x = 1534236469
Output: 0          # the reverse overflows
```

## Constraints

- `-2^31 <= x <= 2^31 - 1`

## Hints

- Peel digits off with `% 10` and `// 10`, handling the sign separately, and check for overflow before returning.
''',
      r'''
class Solution:
    def reverse(self, x: int) -> int:
        pass
''',
      r'''
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
''',
      [([123], 321), ([-123], -321), ([120], 21), ([0], 0), ([1534236469], 0), ([-2147483648], 0), ([2147483647], 0),
       ([1463847412], 2147483641), ([100], 1), ([-10], -1), ([7], 7)],
      gen=lambda rng: [[rng.randint(-1000, 1000)] for _ in range(4)] + [[rng.randint(-2 ** 31, 2 ** 31 - 1)] for _ in range(6)]
      + [[1000000003], [-1000000003], [1463847412], [-1463847412]],
      small=lambda rng: [rng.randint(-99999, 99999)],
      brute=r'''
class Solution:
    def reverse(self, x):
        s = str(abs(x))[::-1]
        r = int(s) * (-1 if x < 0 else 1)
        return r if -(2 ** 31) <= r < 2 ** 31 else 0
'''),
]

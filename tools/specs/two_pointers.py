from spec import P

CATEGORY = "two-pointers"

_CLEAN = "".join(chr(c) for c in range(48, 58)) + "abcXYZ"


def _palins(rng):
    out = []
    for n in (3, 8, 20, 5000):
        half = "".join(rng.choice(_CLEAN) for _ in range(n))
        s = half + rng.choice(["", rng.choice(_CLEAN)]) + half[::-1].swapcase()
        noisy = "".join(c + (rng.choice(" ,.:;!_-") if rng.random() < 0.3 else "") for c in s)
        out.append([noisy])
        out.append([noisy[:-1] + ("z" if noisy[-1] != "z" else "y")])
    for _ in range(4):
        out.append(["".join(rng.choice("aAb1 ,.") for _ in range(rng.randint(1, 9)))])
    return out


def _two_sum2(rng):
    out = []
    for n in (4, 30, 10000):
        nums = sorted(rng.sample(range(-10 * n, 10 * n), n))
        out.append([nums, nums[-1] + nums[-2] if n == 10000 else nums[rng.randrange(n - 1)] + nums[-1]])
    return out


def _three_sum(rng):
    out = [[[rng.randint(-5, 5) for _ in range(rng.randint(3, 14))]] for _ in range(4)]
    out.append([[0] * 3000])
    out.append([[rng.randint(-100000, 100000) for _ in range(2000)]])
    out.append([[rng.choice([-1, 0, 1]) for _ in range(300)]])
    return out


PROBLEMS = [
    P(10, "Valid Palindrome", "Easy", "isPalindrome",
      r'''
Given a string `s`, decide whether it reads the same forwards and backwards after you throw away every character that is not a letter or digit and ignore upper/lower case.

Return `True` if it is a palindrome under those rules, otherwise `False`.

## Examples

```
Input:  s = "Was it a car or a cat I saw?"
Output: True

Input:  s = "tab a cat"
Output: False
```

## Constraints

- `1 <= len(s) <= 20000`
- `s` contains printable ASCII characters.

## Hints

- Use one pointer at each end and move them towards each other, skipping characters that do not count.
- `str.isalnum()` tells you whether a character counts.
''',
      r'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        pass
''',
      r'''
class Solution:
    def isPalindrome(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
''',
      [(["Was it a car or a cat I saw?"], True), (["tab a cat"], False), ([" "], True), (["a."], True),
       (["0P"], False), (["A man, a plan, a canal: Panama"], True), (["race a car"], False),
       (["ab_a"], True), (["ab"], False), ([".,"], True), (["No lemon, no melon"], True)],
      gen=_palins,
      small=lambda rng: ["".join(rng.choice("aAb1 ,.") for _ in range(rng.randint(1, 9)))],
      brute=r'''
class Solution:
    def isPalindrome(self, s):
        t = [c.lower() for c in s if c.isalnum()]
        return t == t[::-1]
'''),

    P(11, "Two Sum II - Input Array Is Sorted", "Medium", "twoSum",
      r'''
`numbers` is a list of integers sorted in non-decreasing order. Find two different positions whose values add up to `target`.

Return the two positions as `[i, j]` using 1-based indexing with `i < j`. At least one valid pair exists; if there are several, any one is accepted.

Use only O(1) extra space.

## Examples

```
Input:  numbers = [1, 2, 3, 4], target = 3
Output: [1, 2]

Input:  numbers = [2, 7, 11, 15], target = 9
Output: [1, 2]
```

## Constraints

- `2 <= len(numbers) <= 10000`
- `-10^6 <= numbers[i] <= 10^6`
- `numbers` is sorted in non-decreasing order.

## Hints

- Start with one pointer at each end. If the sum is too big, which pointer should move?
''',
      r'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pass
''',
      r'''
class Solution:
    def twoSum(self, numbers, target):
        i, j = 0, len(numbers) - 1
        while i < j:
            s = numbers[i] + numbers[j]
            if s == target:
                return [i + 1, j + 1]
            if s < target:
                i += 1
            else:
                j -= 1
''',
      [([[1, 2, 3, 4], 3], [1, 2]), ([[2, 7, 11, 15], 9], [1, 2]), ([[2, 3, 4], 6], [1, 3]),
       ([[-1, 0], -1], [1, 2]), ([[1, 3, 4, 5, 7, 10, 11], 9], [3, 4]), ([[5, 25, 75], 100], [2, 3]),
       ([[-5, -3, 0, 3, 8], 0], [2, 4]), ([[0, 0, 3, 4], 0], [1, 2]), ([[1, 1, 1, 1], 2], [1, 2])],
      checker=r'''
def check(args, got, expected, inputs):
    nums, target = args
    ok = isinstance(got, list) and len(got) == 2 and all(type(x) is int for x in got)
    if not ok:
        return "return a list of two integer positions"
    i, j = got
    if not 1 <= i < j <= len(nums):
        return "positions must be 1-based with i < j"
    if nums[i - 1] + nums[j - 1] != target:
        return f"numbers[{i}] + numbers[{j}] = {nums[i - 1] + nums[j - 1]}, not {target}"
    return True
''',
      gen=_two_sum2,
      small=lambda rng: (lambda n: [n, n[rng.randrange(len(n) - 1)] + n[-1]])(
          sorted(rng.randint(-9, 9) for _ in range(rng.randint(2, 8)))),
      brute=r'''
class Solution:
    def twoSum(self, numbers, target):
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
'''),

    P(12, "3Sum", "Medium", "threeSum",
      r'''
Given a list of integers `nums`, return every distinct triplet `[a, b, c]` of values taken from three different positions such that `a + b + c == 0`.

The same combination of values must not appear twice in the answer. The triplets and the numbers inside them may be returned in any order.

## Examples

```
Input:  nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]

Input:  nums = [0, 1, 1]
Output: []
```

## Constraints

- `3 <= len(nums) <= 3000`
- `-10^5 <= nums[i] <= 10^5`

## Hints

- Sort first. Fix one number, then look for the other two with two pointers.
- Skip equal neighbours to avoid duplicate triplets.
''',
      r'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pass
''',
      r'''
class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        out = []
        for i, a in enumerate(nums):
            if a > 0:
                break
            if i and a == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = a + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    out.append([a, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return out
''',
      [([[-1, 0, 1, 2, -1, -4]], [[-1, -1, 2], [-1, 0, 1]]), ([[0, 1, 1]], []), ([[0, 0, 0]], [[0, 0, 0]]),
       ([[0, 0, 0, 0]], [[0, 0, 0]]), ([[-2, 0, 1, 1, 2]], [[-2, 0, 2], [-2, 1, 1]]), ([[1, 2, -2, -1]], []),
       ([[3, 0, -2, -1, 1, 2]], [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]), ([[-1, -1, -1, 2]], [[-1, -1, 2]]),
       ([[1, 2, 3]], [])],
      compare="unordered_nested",
      gen=_three_sum,
      small=lambda rng: [[rng.randint(-4, 4) for _ in range(rng.randint(3, 9))]],
      brute=r'''
class Solution:
    def threeSum(self, nums):
        found = set()
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        found.add(tuple(sorted((nums[i], nums[j], nums[k]))))
        return [list(t) for t in found]
'''),

    P(13, "Container With Most Water", "Medium", "maxArea",
      r'''
`heights[i]` is the height of a vertical line drawn at position `i`. Pick any two lines; together with the x-axis they form a container whose water level is limited by the shorter line.

Return the largest amount of water a container can hold (width times the shorter height).

## Examples

```
Input:  heights = [1, 7, 2, 5, 4, 7, 3, 6]
Output: 36

Input:  heights = [2, 2, 2]
Output: 4
```

## Constraints

- `2 <= len(heights) <= 12000`
- `0 <= heights[i] <= 10000`

## Hints

- Start with the widest container. Moving which pointer could ever help?
''',
      r'''
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        pass
''',
      r'''
class Solution:
    def maxArea(self, heights):
        i, j = 0, len(heights) - 1
        best = 0
        while i < j:
            best = max(best, (j - i) * min(heights[i], heights[j]))
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return best
''',
      [([[1, 7, 2, 5, 4, 7, 3, 6]], 36), ([[2, 2, 2]], 4), ([[1, 1]], 1), ([[0, 0]], 0),
       ([[4, 3, 2, 1, 4]], 16), ([[1, 8, 6, 2, 5, 4, 8, 3, 7]], 49), ([[2, 3, 4, 5, 18, 17, 6]], 17),
       ([[5, 0, 0, 0, 5]], 20)],
      gen=lambda rng: [[[rng.randint(0, 20) for _ in range(rng.randint(2, 12))]] for _ in range(3)]
      + [[[rng.randint(0, 10000) for _ in range(12000)]]]
      + [[list(range(1, 6001)) + list(range(6000, 0, -1))]],
      small=lambda rng: [[rng.randint(0, 9) for _ in range(rng.randint(2, 9))]],
      brute=r'''
class Solution:
    def maxArea(self, heights):
        best = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                best = max(best, (j - i) * min(heights[i], heights[j]))
        return best
'''),

    P(14, "Trapping Rain Water", "Hard", "trap",
      r'''
`height[i]` is the height of a bar of width 1 at position `i`. After it rains, water collects in the gaps between bars.

Return the total number of units of water that remain trapped.

## Examples

```
Input:  height = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
Output: 9

Input:  height = [4, 2, 0, 3, 2, 5]
Output: 9
```

## Constraints

- `1 <= len(height) <= 10000`
- `0 <= height[i] <= 1000`

## Hints

- The water above bar `i` depends on the tallest bar to its left and the tallest to its right.
- Can you do it in one pass with two pointers and O(1) space?
''',
      r'''
class Solution:
    def trap(self, height: List[int]) -> int:
        pass
''',
      r'''
class Solution:
    def trap(self, height):
        i, j = 0, len(height) - 1
        left = right = water = 0
        while i < j:
            if height[i] < height[j]:
                left = max(left, height[i])
                water += left - height[i]
                i += 1
            else:
                right = max(right, height[j])
                water += right - height[j]
                j -= 1
        return water
''',
      [([[0, 2, 0, 3, 1, 0, 1, 3, 2, 1]], 9), ([[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]], 6),
       ([[4, 2, 0, 3, 2, 5]], 9), ([[1, 2, 3]], 0), ([[3, 2, 1]], 0), ([[2, 0, 2]], 2), ([[5]], 0),
       ([[0, 0]], 0), ([[3, 0, 0, 0, 3]], 9), ([[5, 4, 1, 2]], 1)],
      gen=lambda rng: [[[rng.randint(0, 6) for _ in range(rng.randint(1, 14))]] for _ in range(3)]
      + [[[rng.randint(0, 1000) for _ in range(10000)]]]
      + [[[1000] + [0] * 9998 + [1000]]],
      small=lambda rng: [[rng.randint(0, 6) for _ in range(rng.randint(1, 10))]],
      brute=r'''
class Solution:
    def trap(self, height):
        total = 0
        for i, h in enumerate(height):
            total += min(max(height[:i + 1]), max(height[i:])) - h
        return total
'''),
]

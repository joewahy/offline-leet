# 109. Longest Increasing Subsequence (Medium)

Return the length of the longest strictly increasing subsequence of `nums`. A subsequence keeps the original order but may skip elements.

## Examples

```
Input:  nums = [9, 1, 4, 2, 3, 3, 7]
Output: 4          # 1, 2, 3, 7

Input:  nums = [0, 3, 1, 3, 2, 3]
Output: 4
```

## Constraints

- `1 <= len(nums) <= 2500`
- `-10^4 <= nums[i] <= 10^4`

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. For each element, what is the longest increasing subsequence that ends there?
2. It is 1 plus the best among the earlier, smaller elements. This gives an O(n^2) solution.
3. For O(n log n), keep a list `tails` where `tails[k]` is the smallest possible last value of an increasing subsequence of length `k + 1`. For each number, binary search (`bisect_left`) its place: replace that entry, or append if it is larger than all of them. The answer is `len(tails)`.

</details>

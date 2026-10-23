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

## Hints

- `O(n^2)`: for each element, look at every earlier smaller element.
- `O(n log n)`: keep the smallest possible tail of an increasing subsequence of each length, and binary search into it.

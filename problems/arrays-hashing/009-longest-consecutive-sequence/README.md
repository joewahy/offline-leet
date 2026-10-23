# 9. Longest Consecutive Sequence (Medium)

Given an unsorted list of integers `nums`, return the length of the longest run of consecutive integers that all appear in the list (for example 4, 5, 6, 7). The numbers do not need to be next to each other in the list.

Your solution must run in O(n) time.

## Examples

```
Input:  nums = [2, 20, 4, 10, 3, 4, 5]
Output: 4          # 2, 3, 4, 5

Input:  nums = [0, 3, 2, 5, 4, 6, 1, 1]
Output: 7          # 0 through 6
```

## Constraints

- `0 <= len(nums) <= 100000`
- `-10^9 <= nums[i] <= 10^9`

## Hints

- Sorting works but is O(n log n).
- Put everything in a set. Only start counting from numbers that have no predecessor (`x - 1` not in the set).

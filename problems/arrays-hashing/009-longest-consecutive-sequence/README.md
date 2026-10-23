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

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Sorting works but costs O(n log n). Which numbers can possibly be the start of a run?
2. Put all numbers in a set. A number `x` starts a run only if `x - 1` is not in the set.
3. From each start, count upward while `x + 1` is in the set. Each number belongs to exactly one run, so the total work is O(n).

</details>

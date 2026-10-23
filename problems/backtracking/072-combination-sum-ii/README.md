# 72. Combination Sum II (Medium)

`candidates` is a list of positive integers that may contain duplicates, and `target` is a positive integer. Return every unique combination of candidates that adds up to `target`. Each candidate may be used at most once, and the result must not contain duplicate combinations.

The combinations, and the numbers inside them, may be returned in any order.

## Examples

```
Input:  candidates = [9, 2, 5, 2, 1], target = 9
Output: [[9], [2, 2, 5]]

Input:  candidates = [2, 5, 2, 1, 2], target = 5
Output: [[1, 2, 2], [5]]
```

## Constraints

- `1 <= len(candidates) <= 30`
- `1 <= candidates[i] <= 50`
- `1 <= target <= 30`

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Each number can be used once, but the input has duplicates, and duplicate combinations are not allowed.
2. Sort the candidates. Recurse with a start index, moving to `i + 1` after choosing index `i`.
3. At the same recursion level, skip a candidate equal to the previous one (`i > start and nums[i] == nums[i - 1]`). Stop the loop when a candidate exceeds the remaining target, since the list is sorted.

</details>

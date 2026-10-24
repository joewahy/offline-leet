# 11. Two Sum II - Input Array Is Sorted (Medium)

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

- `2 <= len(numbers) <= 10^5`
- `-10^6 <= numbers[i] <= 10^6`
- `numbers` is sorted in non-decreasing order.

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. The array is sorted. How does that change the brute force, where you compare every pair?
2. Put one pointer at each end and look at the sum. If it is too small, which pointer can safely move?
3. Sum too small: move the left pointer right. Sum too big: move the right pointer left. Each step discards one element for good, giving O(n) time and O(1) space.

</details>

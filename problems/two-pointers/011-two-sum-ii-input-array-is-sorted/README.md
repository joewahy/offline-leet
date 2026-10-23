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

- `2 <= len(numbers) <= 10000`
- `-10^6 <= numbers[i] <= 10^6`
- `numbers` is sorted in non-decreasing order.

## Hints

- Start with one pointer at each end. If the sum is too big, which pointer should move?

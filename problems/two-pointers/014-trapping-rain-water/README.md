# 14. Trapping Rain Water (Hard)

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

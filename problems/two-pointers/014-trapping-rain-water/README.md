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

- `1 <= len(height) <= 10^5`
- `0 <= height[i] <= 1000`

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Look at one bar. How much water sits on top of it, and which two values decide that?
2. The water above bar `i` is `min(tallest bar to its left, tallest bar to its right) - height[i]`, never below zero.
3. Precompute left and right maxima for O(n) with extra space, or use two pointers that move inward from the shorter side while tracking the maximum seen on each side, for O(1) space.

</details>

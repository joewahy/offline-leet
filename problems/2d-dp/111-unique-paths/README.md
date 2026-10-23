# 111. Unique Paths (Medium)

A robot stands in the top-left cell of an `m x n` grid and wants to reach the bottom-right cell. It can only move right or down.

Return the number of different paths the robot can take.

## Examples

```
Input:  m = 3, n = 6
Output: 21

Input:  m = 3, n = 3
Output: 6
```

## Constraints

- `1 <= m, n <= 100`
- The answer fits in a 32-bit integer for the tested sizes.

## Hints

- The number of ways to reach a cell is the number of ways to reach the cell above plus the cell to the left.
- It is also a combinatorics problem: choose which of the `m + n - 2` moves go down.

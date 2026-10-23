# 137. Spiral Matrix (Medium)

Given an `m x n` matrix, return all of its elements in spiral order: start at the top-left, go right along the top row, then down the right column, then left along the bottom row, then up the left column, and keep spiralling inwards.

## Examples

```
Input:  matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

Input:  matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
```

## Constraints

- `1 <= m, n <= 100`
- `-100 <= matrix[i][j] <= 100`

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Walk along the outside, then do the same for the inside. What do you need to remember?
2. Keep four boundaries: top, bottom, left and right. Walk each side, then move the boundaries inwards.
3. After walking the top row and the right column, only walk the bottom row if `top < bottom`, and the left column if `left < right`, so a single leftover row or column is not visited twice. Stop when the boundaries cross.

</details>

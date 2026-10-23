# 57. Kth Smallest Element in a BST (Medium)

Given the root of a binary search tree and an integer `k`, return the `k`-th smallest value in the tree (counting from 1).

## Examples

```
Input:  root = [3, 1, 4, null, 2], k = 1
Output: 1

Input:  root = [5, 3, 6, 2, 4, null, null, 1], k = 3
Output: 3
```

## Constraints

- `1 <= k <= number of nodes <= 3000`
- `0 <= node.val <= 10^4`

## Hints

- An in-order traversal of a BST visits values in sorted order. Stop after `k` nodes.

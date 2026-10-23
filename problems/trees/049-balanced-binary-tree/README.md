# 49. Balanced Binary Tree (Easy)

A binary tree is height-balanced if, for every node, the heights of its left and right subtrees differ by at most 1.

Return `True` if the given tree is height-balanced, otherwise `False`. An empty tree is balanced.

## Examples

```
Input:  root = [1, 2, 3, null, null, 4]
Output: True

Input:  root = [1, 2, 3, null, null, 4, null, 5]
Output: False
```

## Constraints

- `0 <= number of nodes <= 3000`
- `-100 <= node.val <= 100`

## Hints

- Compute heights bottom up and return a sentinel (like `-1`) as soon as a subtree is unbalanced, so each node is visited once.

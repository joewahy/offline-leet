# 55. Count Good Nodes in Binary Tree (Medium)

In a binary tree, a node `X` is good if no node on the path from the root to `X` has a value greater than `X`. The root is always good.

Return the number of good nodes in the tree.

## Examples

```
Input:  root = [2, 1, 1, 3, null, 1, 5]
Output: 3

Input:  root = [3, 3, null, 4, 2]
Output: 3
```

## Constraints

- `1 <= number of nodes <= 3000`
- `-10000 <= node.val <= 10000`

## Hints

- Carry the maximum value seen so far down the recursion.

# 52. Lowest Common Ancestor of a Binary Search Tree (Medium)

Given a binary search tree and two of its nodes `p` and `q`, return their lowest common ancestor: the deepest node that has both `p` and `q` as descendants. A node counts as a descendant of itself.

In the tests, `p` and `q` are given as values; your function receives the matching nodes, and the answer is the value of the node you return.

## Examples

```
Input:  root = [5, 3, 8, 1, 4, 7, 9, null, 2], p = 3, q = 8
Output: 5

Input:  root = [5, 3, 8, 1, 4, 7, 9, null, 2], p = 3, q = 4
Output: 3
```

## Constraints

- `2 <= number of nodes <= 3000`
- All node values are unique, and `p != q`, and both exist in the tree.

## Hints

- If both values are smaller than the current node, go left; if both are larger, go right. Otherwise the current node splits them.

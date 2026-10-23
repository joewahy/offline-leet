# 46. Invert Binary Tree (Easy)

Given the root of a binary tree, mirror it: swap the left and right child of every node. Return the root of the inverted tree.

Trees in the tests are written in level order, with `null` for a missing child.

## Examples

```
Input:  root = [1, 2, 3, 4, 5, 6, 7]
Output: [1, 3, 2, 7, 6, 5, 4]

Input:  root = [3, 2, 1]
Output: [3, 1, 2]
```

## Constraints

- `0 <= number of nodes <= 3000`
- `-100 <= node.val <= 100`

## Hints

- Invert the two subtrees, then swap them. Recursion or an explicit queue both work.

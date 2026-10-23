# 56. Validate Binary Search Tree (Medium)

Return `True` if the given binary tree is a valid binary search tree, otherwise `False`.

A valid BST has, for every node, only smaller values in its left subtree and only larger values in its right subtree (equal values are not allowed), and both subtrees are valid BSTs too.

## Examples

```
Input:  root = [2, 1, 3]
Output: True

Input:  root = [5, 1, 4, null, null, 3, 6]
Output: False
```

## Constraints

- `1 <= number of nodes <= 3000`
- `-2^31 <= node.val <= 2^31 - 1`

## Hints

- Checking only a node's direct children is not enough. Pass down the allowed range `(low, high)` for each node.

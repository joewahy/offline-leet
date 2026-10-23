# 48. Diameter of Binary Tree (Easy)

The diameter of a binary tree is the number of edges on the longest path between any two of its nodes. The path may or may not go through the root.

Return the diameter of the given tree.

## Examples

```
Input:  root = [1, null, 2, 3, 4, 5]
Output: 3

Input:  root = [1, 2, 3]
Output: 2
```

## Constraints

- `1 <= number of nodes <= 3000`
- `-100 <= node.val <= 100`

## Hints

- At each node, the longest path through it is `height(left) + height(right)`. Compute heights and track the best sum in one traversal.

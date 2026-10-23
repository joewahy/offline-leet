# 47. Maximum Depth of Binary Tree (Easy)

Return the depth of a binary tree: the number of nodes on the longest path from the root down to a leaf. An empty tree has depth `0`.

## Examples

```
Input:  root = [1, 2, 3, null, null, 4]
Output: 3

Input:  root = []
Output: 0
```

## Constraints

- `0 <= number of nodes <= 3000`
- `-100 <= node.val <= 100`

## Hints

- The depth of a node is `1 + max(depth(left), depth(right))`.

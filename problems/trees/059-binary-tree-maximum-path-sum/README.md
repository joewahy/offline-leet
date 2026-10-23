# 59. Binary Tree Maximum Path Sum (Hard)

A path in a binary tree is a sequence of nodes where each pair of neighbours is connected by an edge, and no node appears twice. A path does not need to pass through the root, and it must contain at least one node.

Return the largest possible sum of the values along any path.

## Examples

```
Input:  root = [1, 2, 3]
Output: 6

Input:  root = [-10, 9, 20, null, null, 15, 7]
Output: 42
```

## Constraints

- `1 <= number of nodes <= 3000`
- `-1000 <= node.val <= 1000`

## Hints

- For each node, the best path that turns there is `node.val + best downward gain from left + best downward gain from right`. Ignore negative gains.

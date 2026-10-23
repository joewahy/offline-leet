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

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. A path may bend at one node, using a branch from its left and a branch from its right. But a path that continues upward can only use one branch.
2. For each node compute the best downward path starting at it, and separately the best path that bends at it.
3. Let `gain(node) = node.val + max(0, gain(left), gain(right))` for the upward path (ignore negative branches). The best path bending at a node is `node.val + max(0, gain(left)) + max(0, gain(right))`. Keep a running maximum of that.

</details>

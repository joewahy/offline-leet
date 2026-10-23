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

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Whether a node is good depends only on the nodes above it on its own path.
2. Pass the largest value seen so far down the recursion.
3. At each node, count it as good if `node.val >= max_so_far`. Then recurse into both children with `max(max_so_far, node.val)`. The root is always good.

</details>

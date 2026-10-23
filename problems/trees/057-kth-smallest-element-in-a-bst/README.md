# 57. Kth Smallest Element in a BST (Medium)

Given the root of a binary search tree and an integer `k`, return the `k`-th smallest value in the tree (counting from 1).

## Examples

```
Input:  root = [3, 1, 4, null, 2], k = 1
Output: 1

Input:  root = [5, 3, 6, 2, 4, null, null, 1], k = 3
Output: 3
```

## Constraints

- `1 <= k <= number of nodes <= 3000`
- `0 <= node.val <= 10^4`

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. An in-order traversal of a BST visits the values in sorted order.
2. Traverse in order and stop as soon as you have visited `k` nodes.
3. Use an iterative in-order traversal with a stack: go left as far as possible, pop a node and decrement `k`, return when `k` reaches zero, then move to the right child. It stops early and uses O(h + k) time.

</details>

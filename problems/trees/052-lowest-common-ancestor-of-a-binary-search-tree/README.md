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

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Use the BST ordering. If both values are smaller than the current node, where must they be? What if both are larger?
2. If both values are smaller than the current node, go left. If both are larger, go right.
3. The first node where the two values split (one is smaller or equal, the other larger or equal) is the lowest common ancestor. An iterative loop uses O(1) space.

</details>

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

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Comparing a node only with its direct children is not enough: a deeper node must also respect ancestors further up.
2. Each node must lie strictly inside a range `(low, high)` that gets narrower as you go down.
3. Start with `(-inf, +inf)`. Going left, the new upper bound is the node's value. Going right, the new lower bound is the node's value. Fail if a value falls outside its range. An in-order traversal that is strictly increasing also works.

</details>

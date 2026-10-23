# 60. Serialize and Deserialize Binary Tree (Hard)

Design an algorithm that converts a binary tree into a string (`serialize`) and rebuilds the exact same tree from that string (`deserialize`).

The two methods are called on separate `Codec` objects, so everything needed to rebuild the tree must be inside the string. The format is up to you. `serialize` must return a `str`.

The tree you get back must have the same shape and the same values as the original.

## Examples

```
Input:  root = [1, 2, 3, null, null, 4, 5]
deserialize(serialize(root)) must give back [1, 2, 3, null, null, 4, 5]

Input:  root = []
deserialize(serialize(root)) must give back []
```

## Constraints

- `0 <= number of nodes <= 3000`
- `-1000 <= node.val <= 1000`

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. A traversal alone does not identify a tree unless you also record where children are missing.
2. Do a preorder traversal and write a marker such as `N` for every missing child. The result describes the shape uniquely.
3. Join the values with a separator, like `1,2,N,N,3,N,N`. To deserialize, read the tokens in order: a marker returns `None`, otherwise create a node and recursively build its left child, then its right child, from the next tokens.

</details>

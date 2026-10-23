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

## Hints

- A preorder traversal that also records the empty children (for example as `N`) is enough to rebuild the tree uniquely.

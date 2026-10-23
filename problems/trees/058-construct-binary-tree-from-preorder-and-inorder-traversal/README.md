# 58. Construct Binary Tree from Preorder and Inorder Traversal (Medium)

You are given the preorder and the inorder traversal of a binary tree whose node values are all distinct. Rebuild the tree and return its root.

(Preorder visits root, left subtree, right subtree. Inorder visits left subtree, root, right subtree.)

## Examples

```
Input:  preorder = [3, 9, 20, 15, 7], inorder = [9, 3, 15, 20, 7]
Output: [3, 9, 20, null, null, 15, 7]

Input:  preorder = [1, 2], inorder = [1, 2]
Output: [1, null, 2]
```

## Constraints

- `1 <= len(preorder) == len(inorder) <= 3000`
- `-3000 <= value <= 3000`, all distinct

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. In preorder the first value is always the root. Where does that value sit in the inorder list?
2. Everything left of the root in the inorder list is the left subtree, and everything right of it is the right subtree. Their sizes tell you how to split the preorder list too.
3. Store each value's inorder index in a dictionary. Recurse on inorder ranges, consuming preorder values one at a time: build the left subtree first, then the right. That is O(n).

</details>

from leet.structures import TreeNode, tree_to
from spec import P, TREE_HDR

CATEGORY = "trees"

TR = ["tree"]


def _rand_root(rng, n, lo=-20, hi=20):
    if n == 0:
        return None
    root = TreeNode(rng.randint(lo, hi))
    free = [(root, "left"), (root, "right")]
    for _ in range(n - 1):
        i = rng.randrange(len(free))
        free[i], free[-1] = free[-1], free[i]
        node, side = free.pop()
        child = TreeNode(rng.randint(lo, hi))
        setattr(node, side, child)
        free += [(child, "left"), (child, "right")]
    return root


def _rand(rng, n, lo=-20, hi=20):
    return tree_to(_rand_root(rng, n, lo, hi))


def _chain(rng, n):
    root = cur = TreeNode(rng.randint(-9, 9))
    for _ in range(n - 1):
        nxt = TreeNode(rng.randint(-9, 9))
        setattr(cur, rng.choice(["left", "right"]), nxt)
        cur = nxt
    return tree_to(root)


def _bst_root(rng, n, lo=-100000, hi=100000):
    vals = rng.sample(range(lo, hi), n)
    root = None
    for v in vals:
        node = TreeNode(v)
        if root is None:
            root = node
            continue
        cur = root
        while True:
            side = "left" if v < cur.val else "right"
            if getattr(cur, side) is None:
                setattr(cur, side, node)
                break
            cur = getattr(cur, side)
    return root, sorted(vals)


def _bst(rng, n, lo=-100000, hi=100000):
    root, vals = _bst_root(rng, n, lo, hi)
    return tree_to(root), vals


def _walk(root):
    out, stack = [], [root] if root else []
    while stack:
        node = stack.pop()
        out.append(node)
        stack += [c for c in (node.left, node.right) if c]
    return out


def _tweak(rng, enc):
    enc = list(enc)
    idx = [i for i, v in enumerate(enc) if v is not None]
    i = rng.choice(idx)
    enc[i] += 1
    return enc


def _same_gen(rng):
    out = []
    for n in (1, 4, 9, 15):
        t = _rand(rng, n)
        out.append([t, list(t)])
        out.append([t, _tweak(rng, t)])
    big = _rand(rng, 3000)
    out += [[big, list(big)], [big, _tweak(rng, big)]]
    return out


def _subtree_gen(rng):
    out = []
    for n in (3, 8, 15, 40):
        root = _rand_root(rng, n, 0, 3)
        sub = tree_to(rng.choice(_walk(root)))
        out.append([tree_to(root), sub])
        out.append([tree_to(root), _tweak(rng, sub)])
    big = _rand_root(rng, 2000, 0, 1)
    out.append([tree_to(big), tree_to(rng.choice(_walk(big)))])
    return out


def _lca_gen(rng):
    out = []
    for n in (2, 5, 12, 40, 3000):
        enc, vals = _bst(rng, n, -10000, 10000)
        p, q = rng.sample(vals, 2)
        out.append([enc, p, q])
    chain = list(range(1, 2001))
    root = TreeNode(chain[0])
    cur = root
    for v in chain[1:]:
        cur.right = TreeNode(v)
        cur = cur.right
    out.append([tree_to(root), 1999, 2000])
    return out


def _traversals(root):
    pre, ino = [], []

    def go(node):
        if node:
            pre.append(node.val)
            go(node.left)
            ino.append(node.val)
            go(node.right)

    go(root)
    return pre, ino


def _build_gen(rng):
    out = []
    for n in (1, 2, 5, 12, 40, 1500):
        root = _rand_root(rng, n)
        vals = rng.sample(range(-5000, 5000), n)
        for node, v in zip(_walk(root), vals):
            node.val = v
        out.append(list(_traversals(root)))
    return out


def _build_small(rng):
    root = _rand_root(rng, rng.randint(1, 8))
    for node, v in zip(_walk(root), rng.sample(range(-30, 30), 8)):
        node.val = v
    return list(_traversals(root))


def _codec_gen(rng):
    return [[_rand(rng, n, -1000, 1000)] for n in (3, 10, 40, 500)] + [[_chain(rng, 2000)], [[]], [[7]]]


PROBLEMS = [
    P(46, "Invert Binary Tree", "Easy", "invertTree",
      r'''
Given the root of a binary tree, mirror it: swap the left and right child of every node. Return the root of the inverted tree.

Trees in the tests are written in level order, with `null` for a missing child.

## Examples

```
Input:  root = [1, 2, 3, 4, 5, 6, 7]
Output: [1, 3, 2, 7, 6, 5, 4]

Input:  root = [3, 2, 1]
Output: [3, 1, 2]
```

## Constraints

- `0 <= number of nodes <= 3000`
- `-100 <= node.val <= 100`

## Hints

- Invert the two subtrees, then swap them. Recursion or an explicit queue both work.
''',
      TREE_HDR + r'''
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        pass
''',
      r'''
class Solution:
    def invertTree(self, root):
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
''',
      [([[1, 2, 3, 4, 5, 6, 7]], [1, 3, 2, 7, 6, 5, 4]), ([[3, 2, 1]], [3, 1, 2]), ([[]], []), ([[1]], [1]),
       ([[1, 2]], [1, None, 2]), ([[1, None, 2]], [1, 2]), ([[4, 2, 7, 1, 3, 6, 9]], [4, 7, 2, 9, 6, 3, 1])],
      arg_types=TR, return_type="tree",
      gen=lambda rng: [[_rand(rng, n, -100, 100)] for n in (3, 8, 15, 40)] + [[_rand(rng, 3000, -100, 100)], [_chain(rng, 3000)]],
      small=lambda rng: [_rand(rng, rng.randint(0, 9))],
      brute=r'''
from collections import deque


class Solution:
    def invertTree(self, root):
        q = deque([root] if root else [])
        while q:
            node = q.popleft()
            node.left, node.right = node.right, node.left
            q.extend(c for c in (node.left, node.right) if c)
        return root
'''),

    P(47, "Maximum Depth of Binary Tree", "Easy", "maxDepth",
      r'''
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
''',
      TREE_HDR + r'''
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        pass
''',
      r'''
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
''',
      [([[1, 2, 3, None, None, 4]], 3), ([[]], 0), ([[1]], 1), ([[1, 2]], 2), ([[1, None, 2, None, 3]], 3),
       ([[3, 9, 20, None, None, 15, 7]], 3)],
      arg_types=TR,
      gen=lambda rng: [[_rand(rng, n)] for n in (4, 9, 20)] + [[_rand(rng, 3000)], [_chain(rng, 3000)]],
      small=lambda rng: [_rand(rng, rng.randint(0, 10))],
      brute=r'''
class Solution:
    def maxDepth(self, root):
        level, depth = [root] if root else [], 0
        while level:
            depth += 1
            level = [c for n in level for c in (n.left, n.right) if c]
        return depth
'''),

    P(48, "Diameter of Binary Tree", "Easy", "diameterOfBinaryTree",
      r'''
The diameter of a binary tree is the number of edges on the longest path between any two of its nodes. The path may or may not go through the root.

Return the diameter of the given tree.

## Examples

```
Input:  root = [1, null, 2, 3, 4, 5]
Output: 3

Input:  root = [1, 2, 3]
Output: 2
```

## Constraints

- `1 <= number of nodes <= 3000`
- `-100 <= node.val <= 100`

## Hints

- At each node, the longest path through it is `height(left) + height(right)`. Compute heights and track the best sum in one traversal.
''',
      TREE_HDR + r'''
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        pass
''',
      r'''
class Solution:
    def diameterOfBinaryTree(self, root):
        best = 0

        def height(node):
            nonlocal best
            if not node:
                return 0
            l, r = height(node.left), height(node.right)
            best = max(best, l + r)
            return 1 + max(l, r)

        height(root)
        return best
''',
      [([[1, None, 2, 3, 4, 5]], 3), ([[1, 2, 3]], 2), ([[1]], 0), ([[1, 2]], 1), ([[1, 2, 3, 4, 5]], 3),
       ([[1, None, 2, None, 3, None, 4]], 3)],
      arg_types=TR,
      gen=lambda rng: [[_rand(rng, n)] for n in (4, 9, 20, 60)] + [[_rand(rng, 3000)], [_chain(rng, 3000)]],
      small=lambda rng: [_rand(rng, rng.randint(1, 10))],
      brute=r'''
from collections import deque


class Solution:
    def diameterOfBinaryTree(self, root):
        adj, stack = {}, [root]
        while stack:
            n = stack.pop()
            adj.setdefault(n, [])
            for c in (n.left, n.right):
                if c:
                    adj.setdefault(c, []).append(n)
                    adj[n].append(c)
                    stack.append(c)
        best = 0
        for start in adj:
            dist, q = {start: 0}, deque([start])
            while q:
                n = q.popleft()
                for m in adj[n]:
                    if m not in dist:
                        dist[m] = dist[n] + 1
                        q.append(m)
            best = max(best, max(dist.values()))
        return best
'''),

    P(49, "Balanced Binary Tree", "Easy", "isBalanced",
      r'''
A binary tree is height-balanced if, for every node, the heights of its left and right subtrees differ by at most 1.

Return `True` if the given tree is height-balanced, otherwise `False`. An empty tree is balanced.

## Examples

```
Input:  root = [1, 2, 3, null, null, 4]
Output: True

Input:  root = [1, 2, 3, null, null, 4, null, 5]
Output: False
```

## Constraints

- `0 <= number of nodes <= 3000`
- `-100 <= node.val <= 100`

## Hints

- Compute heights bottom up and return a sentinel (like `-1`) as soon as a subtree is unbalanced, so each node is visited once.
''',
      TREE_HDR + r'''
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        pass
''',
      r'''
class Solution:
    def isBalanced(self, root):
        def height(node):
            if not node:
                return 0
            l = height(node.left)
            if l < 0:
                return -1
            r = height(node.right)
            if r < 0 or abs(l - r) > 1:
                return -1
            return 1 + max(l, r)

        return height(root) >= 0
''',
      [([[1, 2, 3, None, None, 4]], True), ([[1, 2, 3, None, None, 4, None, 5]], False), ([[]], True), ([[1]], True),
       ([[1, 2, None, 3]], False), ([[1, 2, 2, 3, 3, None, None, 4, 4]], False),
       ([[3, 9, 20, None, None, 15, 7]], True)],
      arg_types=TR,
      gen=lambda rng: [[_rand(rng, n)] for n in (3, 6, 10, 15, 25)] + [[tree_to(_complete(31))], [_chain(rng, 3000)], [_rand(rng, 3000)]],
      small=lambda rng: [_rand(rng, rng.randint(0, 10))],
      brute=r'''
class Solution:
    def isBalanced(self, root):
        def h(n):
            return 0 if not n else 1 + max(h(n.left), h(n.right))

        def ok(n):
            return not n or (abs(h(n.left) - h(n.right)) <= 1 and ok(n.left) and ok(n.right))

        return ok(root)
'''),

    P(50, "Same Tree", "Easy", "isSameTree",
      r'''
Given the roots of two binary trees `p` and `q`, return `True` if they have exactly the same shape and the same value at every position, otherwise `False`.

## Examples

```
Input:  p = [1, 2, 3], q = [1, 2, 3]
Output: True

Input:  p = [4, 7], q = [4, null, 7]
Output: False
```

## Constraints

- `0 <= number of nodes in each tree <= 3000`
- `-100 <= node.val <= 100`

## Hints

- Two trees are the same when both are empty, or the roots match and both pairs of subtrees are the same.
''',
      TREE_HDR + r'''
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pass
''',
      r'''
class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
''',
      [([[1, 2, 3], [1, 2, 3]], True), ([[4, 7], [4, None, 7]], False), ([[1, 2, 3], [1, 3, 2]], False),
       ([[], []], True), ([[1], []], False), ([[1, 2], [1, None, 2]], False), ([[1, None, 2], [1, None, 2]], True)],
      arg_types=["tree", "tree"],
      gen=_same_gen,
      small=lambda rng: (lambda t: [t, rng.choice([list(t), _rand(rng, rng.randint(0, 6)), _tweak(rng, t) if t else t])])(
          _rand(rng, rng.randint(0, 6), 0, 2)),
      brute=r'''
class Solution:
    def isSameTree(self, p, q):
        stack = [(p, q)]
        while stack:
            a, b = stack.pop()
            if (a is None) != (b is None):
                return False
            if a:
                if a.val != b.val:
                    return False
                stack += [(a.left, b.left), (a.right, b.right)]
        return True
'''),

    P(51, "Subtree of Another Tree", "Easy", "isSubtree",
      r'''
Given the roots of two binary trees `root` and `subRoot`, return `True` if `root` contains a node whose subtree (that node and all its descendants) is identical to `subRoot`, otherwise `False`.

## Examples

```
Input:  root = [3, 4, 5, 1, 2], subRoot = [4, 1, 2]
Output: True

Input:  root = [1, 2, 3], subRoot = [1, 2]
Output: False
```

## Constraints

- `1 <= number of nodes in root <= 2000`, `1 <= number of nodes in subRoot <= 1000`
- `-100 <= node.val <= 100`

## Hints

- For each node of `root`, check whether the tree starting there is the same as `subRoot`.
''',
      TREE_HDR + r'''
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        pass
''',
      r'''
class Solution:
    def isSubtree(self, root, subRoot):
        def same(a, b):
            if not a and not b:
                return True
            if not a or not b or a.val != b.val:
                return False
            return same(a.left, b.left) and same(a.right, b.right)

        if not root:
            return False
        return same(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
''',
      [([[1, 2, 3], [2]], True), ([[1, 2, 3], [1, 2]], False), ([[3, 4, 5, 1, 2], [4, 1, 2]], True),
       ([[3, 4, 5, 1, 2, None, None, None, None, 0], [4, 1, 2]], False), ([[1], [1]], True), ([[1, 1], [1]], True),
       ([[1, 2], [2]], True), ([[1, None, 2], [1]], False)],
      arg_types=["tree", "tree"],
      gen=_subtree_gen,
      small=lambda rng: (lambda r: [tree_to(r), tree_to(rng.choice(_walk(r))) if rng.random() < 0.6 else _rand(rng, rng.randint(1, 3), 0, 2)])(
          _rand_root(rng, rng.randint(1, 8), 0, 2)),
      brute=r'''
class Solution:
    def isSubtree(self, root, subRoot):
        def ser(n):
            return "#" if not n else f"({n.val},{ser(n.left)},{ser(n.right)})"

        target = ser(subRoot)
        stack = [root]
        while stack:
            n = stack.pop()
            if n:
                if ser(n) == target:
                    return True
                stack += [n.left, n.right]
        return False
'''),

    P(52, "Lowest Common Ancestor of a Binary Search Tree", "Medium", "lowestCommonAncestor",
      r'''
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

## Hints

- If both values are smaller than the current node, go left; if both are larger, go right. Otherwise the current node splits them.
''',
      r'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pass
''',
      r'''
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        cur = root
        while cur:
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            elif p.val > cur.val and q.val > cur.val:
                cur = cur.right
            else:
                return cur
''',
      [([[5, 3, 8, 1, 4, 7, 9, None, 2], 3, 8], 5), ([[5, 3, 8, 1, 4, 7, 9, None, 2], 1, 4], 3),
       ([[5, 3, 8, 1, 4, 7, 9, None, 2], 2, 4], 3), ([[5, 3, 8, 1, 4, 7, 9, None, 2], 7, 9], 8),
       ([[5, 3, 8, 1, 4, 7, 9, None, 2], 2, 8], 5), ([[5, 3, 8, 1, 4, 7, 9, None, 2], 3, 4], 3),
       ([[2, 1], 2, 1], 2), ([[2, 1], 1, 2], 2), ([[6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 4], 2),
       ([[6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 3, 5], 4), ([[6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 0, 5], 2)],
      arg_types=["tree", "tree_ref", "tree_ref"], return_type="node_val",
      gen=_lca_gen,
      small=lambda rng: (lambda e, v: [e] + rng.sample(v, 2))(*_bst(rng, rng.randint(2, 10), -30, 30)),
      brute=r'''
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        def path(target):
            out, cur = [], root
            while True:
                out.append(cur)
                if cur.val == target.val:
                    return out
                cur = cur.left if target.val < cur.val else cur.right

        a, b = path(p), path(q)
        lca = root
        for x, y in zip(a, b):
            if x is y:
                lca = x
        return lca
'''),

    P(53, "Binary Tree Level Order Traversal", "Medium", "levelOrder",
      r'''
Return the level order traversal of a binary tree: a list of lists, where the `i`-th list holds the values of all nodes at depth `i`, from left to right.

## Examples

```
Input:  root = [3, 9, 20, null, null, 15, 7]
Output: [[3], [9, 20], [15, 7]]

Input:  root = [1]
Output: [[1]]
```

## Constraints

- `0 <= number of nodes <= 3000`
- `-1000 <= node.val <= 1000`

## Hints

- Process the tree one whole level at a time with a queue, using the queue's size at the start of each round.
''',
      TREE_HDR + r'''
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass
''',
      r'''
from collections import deque


class Solution:
    def levelOrder(self, root):
        out = []
        q = deque([root] if root else [])
        while q:
            out.append([])
            for _ in range(len(q)):
                node = q.popleft()
                out[-1].append(node.val)
                q.extend(c for c in (node.left, node.right) if c)
        return out
''',
      [([[3, 9, 20, None, None, 15, 7]], [[3], [9, 20], [15, 7]]), ([[1]], [[1]]), ([[]], []),
       ([[1, 2, 3, 4, 5, 6, 7]], [[1], [2, 3], [4, 5, 6, 7]]), ([[1, 2, None, 3]], [[1], [2], [3]]),
       ([[1, None, 2]], [[1], [2]])],
      arg_types=TR,
      gen=lambda rng: [[_rand(rng, n, -1000, 1000)] for n in (4, 9, 20, 60)] + [[_rand(rng, 3000, -1000, 1000)], [_chain(rng, 3000)]],
      small=lambda rng: [_rand(rng, rng.randint(0, 10))],
      brute=r'''
class Solution:
    def levelOrder(self, root):
        levels = {}

        def go(n, d):
            if n:
                levels.setdefault(d, []).append(n.val)
                go(n.left, d + 1)
                go(n.right, d + 1)

        go(root, 0)
        return [levels[d] for d in sorted(levels)]
'''),

    P(54, "Binary Tree Right Side View", "Medium", "rightSideView",
      r'''
Imagine standing to the right of a binary tree and looking at it. Return the values of the nodes you can see, ordered from top to bottom.

## Examples

```
Input:  root = [1, 2, 3, null, 5, null, 4]
Output: [1, 3, 4]

Input:  root = [1, 2, 3, 4, 5, 6, 7]
Output: [1, 3, 7]
```

## Constraints

- `0 <= number of nodes <= 3000`
- `-100 <= node.val <= 100`

## Hints

- The visible node on each level is the last one in a left-to-right level order traversal.
''',
      TREE_HDR + r'''
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        pass
''',
      r'''
from collections import deque


class Solution:
    def rightSideView(self, root):
        out = []
        q = deque([root] if root else [])
        while q:
            out.append(q[-1].val)
            for _ in range(len(q)):
                node = q.popleft()
                q.extend(c for c in (node.left, node.right) if c)
        return out
''',
      [([[1, 2, 3, None, 5, None, 4]], [1, 3, 4]), ([[1, 2, 3, 4, 5, 6, 7]], [1, 3, 7]), ([[1, None, 3]], [1, 3]),
       ([[]], []), ([[1, 2]], [1, 2]), ([[1, 2, 3, 4]], [1, 3, 4]), ([[1, 2, None, 3, 4]], [1, 2, 4])],
      arg_types=TR,
      gen=lambda rng: [[_rand(rng, n, -100, 100)] for n in (4, 9, 20, 60)] + [[_rand(rng, 3000, -100, 100)], [_chain(rng, 3000)]],
      small=lambda rng: [_rand(rng, rng.randint(0, 10))],
      brute=r'''
class Solution:
    def rightSideView(self, root):
        seen = {}

        def go(n, d):
            if n:
                seen[d] = n.val
                go(n.left, d + 1)
                go(n.right, d + 1)

        go(root, 0)
        return [seen[d] for d in sorted(seen)]
'''),

    P(55, "Count Good Nodes in Binary Tree", "Medium", "goodNodes",
      r'''
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

## Hints

- Carry the maximum value seen so far down the recursion.
''',
      TREE_HDR + r'''
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        pass
''',
      r'''
class Solution:
    def goodNodes(self, root):
        def go(node, biggest):
            if not node:
                return 0
            good = node.val >= biggest
            biggest = max(biggest, node.val)
            return good + go(node.left, biggest) + go(node.right, biggest)

        return go(root, root.val)
''',
      [([[2, 1, 1, 3, None, 1, 5]], 3), ([[3, 3, None, 4, 2]], 3), ([[1]], 1), ([[3, 1, 4, 3, None, 1, 5]], 4),
       ([[5, 4, 3]], 1), ([[1, 2, 3]], 3), ([[-1, -2, -3]], 1)],
      arg_types=TR,
      gen=lambda rng: [[_rand(rng, n, -50, 50)] for n in (4, 9, 20, 60)] + [[_rand(rng, 3000, -10000, 10000)], [_chain(rng, 3000)]],
      small=lambda rng: [_rand(rng, rng.randint(1, 10))],
      brute=r'''
class Solution:
    def goodNodes(self, root):
        count = 0
        stack = [(root, [])]
        while stack:
            node, path = stack.pop()
            if all(v <= node.val for v in path):
                count += 1
            for c in (node.left, node.right):
                if c:
                    stack.append((c, path + [node.val]))
        return count
'''),

    P(56, "Validate Binary Search Tree", "Medium", "isValidBST",
      r'''
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

## Hints

- Checking only a node's direct children is not enough. Pass down the allowed range `(low, high)` for each node.
''',
      TREE_HDR + r'''
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        pass
''',
      r'''
class Solution:
    def isValidBST(self, root):
        def ok(node, low, high):
            if not node:
                return True
            if not low < node.val < high:
                return False
            return ok(node.left, low, node.val) and ok(node.right, node.val, high)

        return ok(root, float("-inf"), float("inf"))
''',
      [([[2, 1, 3]], True), ([[5, 1, 4, None, None, 3, 6]], False), ([[1, 1]], False), ([[2, 2, 2]], False),
       ([[5, 4, 6, None, None, 3, 7]], False), ([[1]], True), ([[10, 5, 15, None, None, 6, 20]], False),
       ([[3, 1, 5, 0, 2, 4, 6]], True), ([[2147483647]], True), ([[-2147483648, None, 2147483647]], True),
       ([[0, -1]], True)],
      arg_types=TR,
      gen=lambda rng: [[_bst(rng, n)[0]] for n in (3, 8, 20)]
      + [[_tweak(rng, _bst(rng, n)[0])] for n in (3, 8, 20)]
      + [[_rand(rng, n, 0, 10)] for n in (3, 6)]
      + [[_bst(rng, 3000)[0]], [_chain_bst(2500)]],
      small=lambda rng: [rng.choice([lambda: _bst(rng, rng.randint(1, 8), -9, 9)[0], lambda: _rand(rng, rng.randint(1, 7), 0, 4)])()],
      brute=r'''
class Solution:
    def isValidBST(self, root):
        vals = []

        def inorder(n):
            if n:
                inorder(n.left)
                vals.append(n.val)
                inorder(n.right)

        inorder(root)
        return all(a < b for a, b in zip(vals, vals[1:]))
'''),

    P(57, "Kth Smallest Element in a BST", "Medium", "kthSmallest",
      r'''
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

## Hints

- An in-order traversal of a BST visits values in sorted order. Stop after `k` nodes.
''',
      TREE_HDR + r'''
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        pass
''',
      r'''
class Solution:
    def kthSmallest(self, root, k):
        stack, cur = [], root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            k -= 1
            if k == 0:
                return cur.val
            cur = cur.right
''',
      [([[3, 1, 4, None, 2], 1], 1), ([[5, 3, 6, 2, 4, None, None, 1], 3], 3), ([[2, 1, 3], 2], 2), ([[1], 1], 1),
       ([[5, 3, 6, 2, 4, None, None, 1], 6], 6), ([[3, 1, 4, None, 2], 4], 4)],
      arg_types=["tree", "plain"],
      gen=lambda rng: [[_bst(rng, n, 0, 10000)[0], rng.randint(1, n)] for n in (3, 8, 20, 60, 3000)] + [[_chain_bst(2500), 2500]],
      small=lambda rng: (lambda n: [_bst(rng, n, 0, 30)[0], rng.randint(1, n)])(rng.randint(1, 9)),
      brute=r'''
class Solution:
    def kthSmallest(self, root, k):
        vals, stack = [], [root]
        while stack:
            n = stack.pop()
            vals.append(n.val)
            stack += [c for c in (n.left, n.right) if c]
        return sorted(vals)[k - 1]
'''),

    P(58, "Construct Binary Tree from Preorder and Inorder Traversal", "Medium", "buildTree",
      r'''
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

## Hints

- The first preorder value is the root. Find it in the inorder list to learn how many nodes belong to the left subtree.
- Store inorder positions in a dictionary so each lookup is O(1).
''',
      TREE_HDR + r'''
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pass
''',
      r'''
class Solution:
    def buildTree(self, preorder, inorder):
        pos = {v: i for i, v in enumerate(inorder)}
        it = iter(preorder)

        def build(lo, hi):
            if lo > hi:
                return None
            val = next(it)
            node = TreeNode(val)
            mid = pos[val]
            node.left = build(lo, mid - 1)
            node.right = build(mid + 1, hi)
            return node

        return build(0, len(inorder) - 1)
''',
      [([[1, 2, 3, 4], [2, 1, 3, 4]], [1, 2, 3, None, None, None, 4]), ([[-1], [-1]], [-1]),
       ([[3, 9, 20, 15, 7], [9, 3, 15, 20, 7]], [3, 9, 20, None, None, 15, 7]), ([[1, 2], [2, 1]], [1, 2]),
       ([[1, 2], [1, 2]], [1, None, 2]), ([[1, 2, 3], [3, 2, 1]], [1, 2, None, 3]),
       ([[1, 2, 3], [1, 2, 3]], [1, None, 2, None, 3])],
      return_type="tree",
      gen=_build_gen, small=_build_small,
      brute=r'''
class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        stack, j = [root], 0
        for val in preorder[1:]:
            node = TreeNode(val)
            top = stack[-1]
            if top.val != inorder[j]:
                top.left = node
            else:
                while stack and stack[-1].val == inorder[j]:
                    top = stack.pop()
                    j += 1
                top.right = node
            stack.append(node)
        return root
'''),

    P(59, "Binary Tree Maximum Path Sum", "Hard", "maxPathSum",
      r'''
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
''',
      TREE_HDR + r'''
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        pass
''',
      r'''
class Solution:
    def maxPathSum(self, root):
        best = float("-inf")

        def gain(node):
            nonlocal best
            if not node:
                return 0
            l, r = max(gain(node.left), 0), max(gain(node.right), 0)
            best = max(best, node.val + l + r)
            return node.val + max(l, r)

        gain(root)
        return best
''',
      [([[1, 2, 3]], 6), ([[-10, 9, 20, None, None, 15, 7]], 42), ([[-3]], -3), ([[2, -1]], 2), ([[-2, -1]], -1),
       ([[1, -2, 3]], 4), ([[5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]], 48), ([[-1, -2, -3]], -1),
       ([[1, 2]], 3)],
      arg_types=TR,
      gen=lambda rng: [[_rand(rng, n, -1000, 1000)] for n in (4, 9, 20, 60)] + [[_rand(rng, 3000, -1000, 1000)], [_chain(rng, 3000)]],
      small=lambda rng: [_rand(rng, rng.randint(1, 9), -9, 9)],
      brute=r'''
class Solution:
    def maxPathSum(self, root):
        adj, stack = {}, [root]
        while stack:
            n = stack.pop()
            adj.setdefault(n, [])
            for c in (n.left, n.right):
                if c:
                    adj.setdefault(c, []).append(n)
                    adj[n].append(c)
                    stack.append(c)
        best = float("-inf")

        def walk(n, seen, total):
            nonlocal best
            best = max(best, total)
            for m in adj[n]:
                if m not in seen:
                    walk(m, seen | {m}, total + m.val)

        for s in adj:
            walk(s, {s}, s.val)
        return best
'''),

    P(60, "Serialize and Deserialize Binary Tree", "Hard", "serialize",
      r'''
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
''',
      r'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        pass

    # Decodes your encoded data to tree.
    def deserialize(self, data):
        """
        :type data: str
        :rtype: TreeNode
        """
        pass
''',
      r'''
class Codec:
    def serialize(self, root):
        out = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node is None:
                out.append("N")
            else:
                out.append(str(node.val))
                stack.append(node.right)
                stack.append(node.left)
        return ",".join(out)

    def deserialize(self, data):
        tokens = iter(data.split(","))

        def build():
            tok = next(tokens)
            if tok == "N":
                return None
            node = TreeNode(int(tok))
            node.left = build()
            node.right = build()
            return node

        return build()
''',
      [([x], x) for x in [[1, 2, 3, None, None, 4, 5], [], [1], [1, None, 2, None, 3], [-1000, 1000],
                          [5, 4, 7, 3, None, 2, None, -1, None, 9]]],
      roundtrip={"type": "tree", "class": "Codec", "encode": "serialize", "decode": "deserialize"},
      arg_types=None,
      gen=_codec_gen),
]


def _complete(n):
    nodes = [TreeNode(i + 1) for i in range(n)]
    for i, node in enumerate(nodes):
        if 2 * i + 1 < n:
            node.left = nodes[2 * i + 1]
        if 2 * i + 2 < n:
            node.right = nodes[2 * i + 2]
    return nodes[0]


def _chain_bst(n):
    root = cur = TreeNode(1)
    for v in range(2, n + 1):
        cur.right = TreeNode(v)
        cur = cur.right
    return tree_to(root)

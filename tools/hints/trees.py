HINTS = {
    52: [
        "Use the BST ordering. If both values are smaller than the current node, where must they be? What if both are larger?",
        "If both values are smaller than the current node, go left. If both are larger, go right.",
        "The first node where the two values split (one is smaller or equal, the other larger or equal) is the lowest common ancestor. An iterative loop uses O(1) space.",
    ],
    53: [
        "You want to visit the tree one level at a time, not depth first. Which structure visits nodes in the order they were discovered?",
        "Use a queue (breadth-first search), starting with the root.",
        "In each round, take `len(queue)` nodes (exactly one level), record their values in one list, and enqueue their children. Use `collections.deque` for O(1) pops from the front.",
    ],
    54: [
        "At each depth, which node would you see from the right?",
        "It is the last node of each level, in left-to-right order.",
        "Do a level order traversal and take the last value of every level. Or do a DFS that visits the right child first and records a node's value the first time it reaches a new depth.",
    ],
    55: [
        "Whether a node is good depends only on the nodes above it on its own path.",
        "Pass the largest value seen so far down the recursion.",
        "At each node, count it as good if `node.val >= max_so_far`. Then recurse into both children with `max(max_so_far, node.val)`. The root is always good.",
    ],
    56: [
        "Comparing a node only with its direct children is not enough: a deeper node must also respect ancestors further up.",
        "Each node must lie strictly inside a range `(low, high)` that gets narrower as you go down.",
        "Start with `(-inf, +inf)`. Going left, the new upper bound is the node's value. Going right, the new lower bound is the node's value. Fail if a value falls outside its range. An in-order traversal that is strictly increasing also works.",
    ],
    57: [
        "An in-order traversal of a BST visits the values in sorted order.",
        "Traverse in order and stop as soon as you have visited `k` nodes.",
        "Use an iterative in-order traversal with a stack: go left as far as possible, pop a node and decrement `k`, return when `k` reaches zero, then move to the right child. It stops early and uses O(h + k) time.",
    ],
    58: [
        "In preorder the first value is always the root. Where does that value sit in the inorder list?",
        "Everything left of the root in the inorder list is the left subtree, and everything right of it is the right subtree. Their sizes tell you how to split the preorder list too.",
        "Store each value's inorder index in a dictionary. Recurse on inorder ranges, consuming preorder values one at a time: build the left subtree first, then the right. That is O(n).",
    ],
    59: [
        "A path may bend at one node, using a branch from its left and a branch from its right. But a path that continues upward can only use one branch.",
        "For each node compute the best downward path starting at it, and separately the best path that bends at it.",
        "Let `gain(node) = node.val + max(0, gain(left), gain(right))` for the upward path (ignore negative branches). The best path bending at a node is `node.val + max(0, gain(left)) + max(0, gain(right))`. Keep a running maximum of that.",
    ],
    60: [
        "A traversal alone does not identify a tree unless you also record where children are missing.",
        "Do a preorder traversal and write a marker such as `N` for every missing child. The result describes the shape uniquely.",
        "Join the values with a separator, like `1,2,N,N,3,N,N`. To deserialize, read the tokens in order: a marker returns `None`, otherwise create a node and recursively build its left child, then its right child, from the next tokens.",
    ],
}

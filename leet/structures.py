"""Data structures LeetCode provides, plus JSON encoders/decoders for test cases.

Test cases are plain JSON. A problem's meta.json names how each argument is
decoded (arg_types) and how the return value is encoded (return_type):

    list_node          [1, 2, 3]                       singly linked list
    list_cycle         [[1, 2, 3], 1]                  list whose tail points at index 1 (-1: no cycle)
    list_of_list_node  [[1, 4], [2, 3]]                several lists
    random_list        [[7, null], [13, 0]]            [value, index of random target]
    tree               [3, 9, 20, null, null, 15, 7]   level order, null for gaps
    tree_ref           5                               the node with that value in the first tree argument
    graph              [[2, 4], [1, 3], [2, 4], [1, 3]]  adjacency list, node i has value i
    intervals          [[0, 30], [5, 10]]              list of Interval(start, end)

The classes match NeetCode's starter code (same constructors and attribute
names). They are predefined in every solution, along with the typing names
Optional/List/Dict/Set/Tuple, so stubs need no imports; see `prelude`.
"""
import typing
from collections import deque

MAX_NODES = 1_000_000


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Node:
    """Graph node (Clone Graph)."""

    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class RandomNode:
    """Linked list node with a random pointer (Copy List with Random Pointer).

    Exposed to solutions under the name `Node`, as on NeetCode.
    """

    def __init__(self, x: int, next: "RandomNode" = None, random: "RandomNode" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Interval:
    """Meeting Rooms intervals."""

    def __init__(self, start, end):
        self.start = start
        self.end = end


def list_from(vals):
    head = None
    for v in reversed(vals):
        head = ListNode(v, head)
    return head


def list_to(head):
    out = []
    while head is not None:
        out.append(head.val)
        head = head.next
        if len(out) > MAX_NODES:
            raise ValueError("returned list is too long or contains a cycle")
    return out


def list_cycle_from(pair):
    vals, pos = pair
    nodes = [ListNode(v) for v in vals]
    for a, b in zip(nodes, nodes[1:]):
        a.next = b
    if nodes and pos >= 0:
        nodes[-1].next = nodes[pos]
    return nodes[0] if nodes else None


def tree_from(vals):
    if not vals:
        return None
    root = TreeNode(vals[0])
    queue = deque([root])
    i = 1
    while queue and i < len(vals):
        node = queue.popleft()
        if vals[i] is not None:
            node.left = TreeNode(vals[i])
            queue.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            queue.append(node.right)
        i += 1
    return root


def tree_to(root):
    out = []
    queue = deque([root] if root is not None else [])
    while queue:
        node = queue.popleft()
        if node is None:
            out.append(None)
        else:
            out.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        if len(out) > 4 * MAX_NODES:
            raise ValueError("returned tree is too large or contains a cycle")
    while out and out[-1] is None:
        out.pop()
    return out


def random_from(pairs):
    nodes = [RandomNode(v) for v, _ in pairs]
    for i, (_, r) in enumerate(pairs):
        if i + 1 < len(nodes):
            nodes[i].next = nodes[i + 1]
        nodes[i].random = None if r is None else nodes[r]
    return nodes[0] if nodes else None


def random_to(head):
    nodes = []
    while head is not None:
        nodes.append(head)
        head = head.next
        if len(nodes) > MAX_NODES:
            raise ValueError("returned list is too long or contains a cycle")
    index = {id(n): i for i, n in enumerate(nodes)}
    return [[n.val, None if n.random is None else index.get(id(n.random), -1)] for n in nodes]


def graph_from(adj):
    if not adj:
        return None
    nodes = [Node(i + 1) for i in range(len(adj))]
    for node, neighbors in zip(nodes, adj):
        node.neighbors = [nodes[j - 1] for j in neighbors]
    return nodes[0]


def graph_to(start):
    if start is None:
        return []
    adj = {}
    queue = deque([start])
    seen = {id(start)}
    while queue:
        node = queue.popleft()
        adj[node.val] = sorted(n.val for n in node.neighbors)
        for n in node.neighbors:
            if id(n) not in seen:
                seen.add(id(n))
                queue.append(n)
    return [adj.get(v, []) for v in range(1, max(adj) + 1)]


def _tree_ref(value, previous):
    root = next(a for a in previous if isinstance(a, TreeNode))
    stack = [root]
    while stack:
        node = stack.pop()
        if node.val == value:
            return node
        stack.extend(c for c in (node.left, node.right) if c is not None)
    raise ValueError(f"value {value} is not in the tree")


def prelude(arg_types):
    """Names every solution can use without importing, as on NeetCode."""
    names = {n: getattr(typing, n) for n in ("Optional", "List", "Dict", "Set", "Tuple", "Deque", "Any")}
    names.update(ListNode=ListNode, TreeNode=TreeNode, Interval=Interval)
    names["Node"] = RandomNode if "random_list" in (arg_types or ()) else Node
    return names


DECODERS = {
    "plain": lambda v, prev: v,
    "list_node": lambda v, prev: list_from(v),
    "list_cycle": lambda v, prev: list_cycle_from(v),
    "list_of_list_node": lambda v, prev: [list_from(x) for x in v],
    "random_list": lambda v, prev: random_from(v),
    "tree": lambda v, prev: tree_from(v),
    "tree_ref": _tree_ref,
    "graph": lambda v, prev: graph_from(v),
    "intervals": lambda v, prev: [Interval(a, b) for a, b in v],
}

ENCODERS = {
    "plain": lambda v: v,
    "list_node": list_to,
    "random_list": random_to,
    "tree": tree_to,
    "node_val": lambda n: None if n is None else n.val,
    "graph": graph_to,
}


def decode(kind, value, previous):
    return DECODERS[kind](value, previous)


def encode(kind, value):
    return ENCODERS[kind](value)

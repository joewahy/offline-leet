from spec import P, LIST_HDR

CATEGORY = "linked-list"

LN = ["list_node"]


def _vals(rng, n, lo=-9, hi=9):
    return [rng.randint(lo, hi) for _ in range(n)]


def _sorted(rng, n, lo=-20, hi=20):
    return sorted(rng.randint(lo, hi) for _ in range(n))


def _cycle_gen(rng):
    out = [[[_vals(rng, n), rng.randint(-1, n - 1)]] for n in (1, 2, 5, 9)]
    out.append([[_vals(rng, 5000), 2500]])
    out.append([[_vals(rng, 5000), -1]])
    return out


def _random_list(rng, n):
    return [[rng.randint(-10, 10), rng.choice([None] + list(range(n)))] for _ in range(n)]


def _dup_array(rng, n):
    d = rng.randint(1, n)
    c = rng.randint(2, min(4, n + 1))
    others = rng.sample([v for v in range(1, n + 1) if v != d], n + 1 - c)
    nums = [d] * c + others
    rng.shuffle(nums)
    return nums


def _dup_gen(rng):
    return [[_dup_array(rng, n)] for n in (1, 3, 8, 30, 10000)]


def _dup_small(rng):
    return [_dup_array(rng, rng.randint(1, 8))]


def _lru(rng, cap, n, keys):
    ops, params = ["LRUCache"], [[cap]]
    for _ in range(n):
        if rng.random() < 0.5:
            ops.append("put")
            params.append([rng.randint(1, keys), rng.randint(0, 99)])
        else:
            ops.append("get")
            params.append([rng.randint(1, keys)])
    return [ops, params]


def _klists(rng, k, m):
    return [[_sorted(rng, rng.randint(0, m), -50, 50) for _ in range(k)]]


PROBLEMS = [
    P(35, "Reverse Linked List", "Easy", "reverseList",
      r'''
Given the head of a singly linked list, reverse the list and return the new head.

## Examples

```
Input:  head = [0, 1, 2, 3]
Output: [3, 2, 1, 0]

Input:  head = []
Output: []
```

## Constraints

- `0 <= number of nodes <= 5000`
- `-5000 <= node.val <= 5000`

## Hints

- Walk the list once, pointing each node back at the node before it.
- You can also do it recursively.
''',
      LIST_HDR + r'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass
''',
      r'''
class Solution:
    def reverseList(self, head):
        prev = None
        while head:
            head.next, prev, head = prev, head, head.next
        return prev
''',
      [([[0, 1, 2, 3]], [3, 2, 1, 0]), ([[]], []), ([[1]], [1]), ([[1, 2]], [2, 1]), ([[5, 4, 3, 2, 1]], [1, 2, 3, 4, 5]),
       ([[-1, 0, 1]], [1, 0, -1])],
      arg_types=LN, return_type="list_node",
      gen=lambda rng: [[_vals(rng, n)] for n in (3, 8, 20, 5000)],
      small=lambda rng: [_vals(rng, rng.randint(0, 8))],
      brute=r'''
class Solution:
    def reverseList(self, head):
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        out = None
        for v in vals:
            out = ListNode(v, out)
        return out
'''),

    P(36, "Merge Two Sorted Lists", "Easy", "mergeTwoLists",
      r'''
You are given the heads of two linked lists that are each sorted in ascending order. Merge them into one sorted list by splicing together the existing nodes, and return the head of the merged list.

## Examples

```
Input:  list1 = [1, 2, 4], list2 = [1, 3, 5]
Output: [1, 1, 2, 3, 4, 5]

Input:  list1 = [], list2 = [0]
Output: [0]
```

## Constraints

- `0 <= length of each list <= 5000`
- `-1000 <= node.val <= 1000`

## Hints

- A dummy head node makes the first insertion the same as every other one.
''',
      LIST_HDR + r'''
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pass
''',
      r'''
class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = tail = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next, list1 = list1, list1.next
            else:
                tail.next, list2 = list2, list2.next
            tail = tail.next
        tail.next = list1 or list2
        return dummy.next
''',
      [([[1, 2, 4], [1, 3, 5]], [1, 1, 2, 3, 4, 5]), ([[], []], []), ([[], [0]], [0]), ([[1, 2], []], [1, 2]),
       ([[1, 3, 5], [2, 4, 6]], [1, 2, 3, 4, 5, 6]), ([[5], [1, 2, 3]], [1, 2, 3, 5]),
       ([[-3, -1], [-2, 0]], [-3, -2, -1, 0]), ([[2, 2], [2]], [2, 2, 2])],
      arg_types=["list_node", "list_node"], return_type="list_node",
      gen=lambda rng: [[_sorted(rng, rng.randint(0, 9)), _sorted(rng, rng.randint(0, 9))] for _ in range(4)]
      + [[_sorted(rng, 5000, -1000, 1000), _sorted(rng, 5000, -1000, 1000)]],
      small=lambda rng: [_sorted(rng, rng.randint(0, 6)), _sorted(rng, rng.randint(0, 6))],
      brute=r'''
class Solution:
    def mergeTwoLists(self, list1, list2):
        vals = []
        for head in (list1, list2):
            while head:
                vals.append(head.val)
                head = head.next
        out = None
        for v in sorted(vals, reverse=True):
            out = ListNode(v, out)
        return out
'''),

    P(37, "Linked List Cycle", "Easy", "hasCycle",
      r'''
Given the head of a linked list, return `True` if the list contains a cycle (some node can be reached again by following `next` pointers), otherwise `False`.

In the tests, a list is described as `[values, pos]`: `pos` is the index of the node the last node points back to, or `-1` for no cycle. `pos` is not passed to your function.

## Examples

```
Input:  values = [1, 2, 3, 4], pos = 1     (4 points back to 2)
Output: True

Input:  values = [1, 2], pos = -1
Output: False
```

## Constraints

- `0 <= number of nodes <= 5000`
- `-10^5 <= node.val <= 10^5`

## Hints

- A set of visited nodes works. Can you do it with O(1) memory using a slow and a fast pointer?
''',
      LIST_HDR + r'''
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pass
''',
      r'''
class Solution:
    def hasCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                return True
        return False
''',
      [([[[1, 2, 3, 4], 1]], True), ([[[1, 2], -1]], False), ([[[1], 0]], True), ([[[], -1]], False),
       ([[[1, 2, 3], 0]], True), ([[[1, 2, 3], 2]], True), ([[[1, 2, 3], -1]], False), ([[[1], -1]], False)],
      arg_types=["list_cycle"],
      gen=_cycle_gen,
      small=lambda rng: [[_vals(rng, (n := rng.randint(0, 7))), rng.randint(-1, max(n - 1, -1))]],
      brute=r'''
class Solution:
    def hasCycle(self, head):
        seen = set()
        while head:
            if id(head) in seen:
                return True
            seen.add(id(head))
            head = head.next
        return False
'''),

    P(38, "Reorder List", "Medium", "reorderList",
      r'''
You are given the head of a singly linked list `L0 -> L1 -> ... -> Ln`. Rearrange it in place into

`L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...`

Do not create new nodes or change node values; only change the `next` pointers. The function returns nothing; the list reachable from `head` afterwards is checked.

## Examples

```
Input:  head = [2, 4, 6, 8]
Output: [2, 8, 4, 6]

Input:  head = [2, 4, 6, 8, 10]
Output: [2, 10, 4, 8, 6]
```

## Constraints

- `1 <= number of nodes <= 5000`
- `1 <= node.val <= 1000`

## Hints

- Find the middle, reverse the second half, then weave the two halves together.
''',
      LIST_HDR + r'''
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        pass
''',
      r'''
class Solution:
    def reorderList(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        second, slow.next = slow.next, None
        prev = None
        while second:
            second.next, prev, second = prev, second, second.next
        first, second = head, prev
        while second:
            first.next, second.next, first, second = second, first.next, first.next, second.next
''',
      [([[2, 4, 6, 8]], [2, 8, 4, 6]), ([[2, 4, 6, 8, 10]], [2, 10, 4, 8, 6]), ([[1]], [1]), ([[1, 2]], [1, 2]),
       ([[1, 2, 3]], [1, 3, 2]), ([[1, 2, 3, 4, 5, 6]], [1, 6, 2, 5, 3, 4]), ([[7, 7, 7, 7]], [7, 7, 7, 7])],
      arg_types=LN, inplace=0,
      gen=lambda rng: [[_vals(rng, n, 1, 99)] for n in (4, 7, 12, 5000)],
      small=lambda rng: [_vals(rng, rng.randint(1, 9), 1, 20)],
      brute=r'''
class Solution:
    def reorderList(self, head):
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        i, j = 0, len(nodes) - 1
        order = []
        while i <= j:
            order.append(nodes[i])
            if i != j:
                order.append(nodes[j])
            i, j = i + 1, j - 1
        for a, b in zip(order, order[1:]):
            a.next = b
        order[-1].next = None
'''),

    P(39, "Remove Nth Node From End of List", "Medium", "removeNthFromEnd",
      r'''
Given the head of a linked list and an integer `n`, remove the `n`-th node counted from the end of the list and return the head of the resulting list.

## Examples

```
Input:  head = [1, 2, 3, 4], n = 2
Output: [1, 2, 4]

Input:  head = [5], n = 1
Output: []
```

## Constraints

- `1 <= number of nodes <= 5000`
- `1 <= n <= number of nodes`
- `1 <= node.val <= 100`

## Hints

- Do it in one pass: move a lead pointer `n` steps ahead, then advance both pointers together.
''',
      LIST_HDR + r'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pass
''',
      r'''
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        lead = trail = dummy
        for _ in range(n):
            lead = lead.next
        while lead.next:
            lead, trail = lead.next, trail.next
        trail.next = trail.next.next
        return dummy.next
''',
      [([[1, 2, 3, 4], 2], [1, 2, 4]), ([[5], 1], []), ([[1, 2], 2], [2]), ([[1, 2], 1], [1]),
       ([[1, 2, 3], 3], [2, 3]), ([[1, 2, 3, 4, 5], 2], [1, 2, 3, 5]), ([[1, 2, 3, 4, 5], 5], [2, 3, 4, 5]),
       ([[1, 2, 3, 4, 5], 1], [1, 2, 3, 4])],
      arg_types=["list_node", "plain"], return_type="list_node",
      gen=lambda rng: [[_vals(rng, n, 1, 99), rng.randint(1, n)] for n in (3, 6, 10, 5000)],
      small=lambda rng: (lambda n: [_vals(rng, n, 1, 20), rng.randint(1, n)])(rng.randint(1, 8)),
      brute=r'''
class Solution:
    def removeNthFromEnd(self, head, n):
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        del vals[len(vals) - n]
        out = None
        for v in reversed(vals):
            out = ListNode(v, out)
        return out
'''),

    P(40, "Copy List with Random Pointer", "Medium", "copyRandomList",
      r'''
Each node of a linked list has a `val`, a `next` pointer, and a `random` pointer that may point to any node in the list or be `None`.

Build a deep copy of the list: create brand-new nodes with the same values, where every `next` and `random` pointer in the copy points to nodes of the copy (never to the original). Return the head of the copy.

In the tests a list is written as `[[val, random_index], ...]`, where `random_index` is the position of the node `random` points to, or `null`.

## Examples

```
Input:  [[7, null], [13, 0], [11, 4], [10, 2], [1, 0]]
Output: a deep copy with the same structure

Input:  [[1, 1], [2, 1]]
Output: a deep copy with the same structure
```

## Constraints

- `0 <= number of nodes <= 1000`
- `-100 <= node.val <= 100`

## Hints

- Map each original node to its copy, then wire up `next` and `random` using the map.
- There is also an O(1) extra space version that interleaves the copies into the original list.
''',
      r'''
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        pass
''',
      r'''
class Solution:
    def copyRandomList(self, head):
        copies = {None: None}
        node = head
        while node:
            copies[node] = Node(node.val)
            node = node.next
        node = head
        while node:
            copies[node].next = copies[node.next]
            copies[node].random = copies[node.random]
            node = node.next
        return copies[head]
''',
      [([x], x) for x in [
          [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]], [[1, 1], [2, 1]], [[3, None], [3, 0], [3, None]], [],
          [[1, None]], [[1, 0]], [[5, 2], [6, 0], [7, 1]]]],
      arg_types=["random_list"], return_type="random_list",
      checker=r'''
from leet.structures import random_to


def check(args, got, expected, inputs):
    original = inputs[0]
    ids = set()
    node = original
    while node is not None:
        ids.add(id(node))
        node = node.next
    if random_to(original) != args[0]:
        return "the original list was modified"
    if random_to(got) != args[0]:
        return "the copy does not have the same values and pointers as the original"
    node = got
    while node is not None:
        if id(node) in ids or (node.random is not None and id(node.random) in ids):
            return "the copy reuses nodes of the original list"
        node = node.next
    return True
''',
      gen=lambda rng: [[_random_list(rng, n)] for n in (2, 5, 12, 1000)],
      small=lambda rng: [_random_list(rng, rng.randint(0, 7))],
      brute=r'''
class Solution:
    def copyRandomList(self, head):
        nodes = []
        node = head
        while node:
            nodes.append(node)
            node = node.next
        copies = [Node(n.val) for n in nodes]
        index = {id(n): i for i, n in enumerate(nodes)}
        for i, n in enumerate(nodes):
            if i + 1 < len(nodes):
                copies[i].next = copies[i + 1]
            if n.random is not None:
                copies[i].random = copies[index[id(n.random)]]
        return copies[0] if copies else None
'''),

    P(41, "Add Two Numbers", "Medium", "addTwoNumbers",
      r'''
Two non-negative integers are stored in two linked lists, one digit per node, with the least significant digit first. For example `342` is stored as `[2, 4, 3]`.

Add the two numbers and return the sum as a linked list in the same format.

## Examples

```
Input:  l1 = [2, 4, 3], l2 = [5, 6, 4]
Output: [7, 0, 8]          # 342 + 465 = 807

Input:  l1 = [9, 9], l2 = [1]
Output: [0, 0, 1]          # 99 + 1 = 100
```

## Constraints

- `1 <= number of nodes in each list <= 3000`
- `0 <= node.val <= 9`
- No list has leading zeros, except the number `0` itself.

## Hints

- Add digit by digit and carry the overflow, like on paper. Don't forget a final carry.
''',
      LIST_HDR + r'''
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pass
''',
      r'''
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = tail = ListNode()
        carry = 0
        while l1 or l2 or carry:
            total = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            carry, digit = divmod(total, 10)
            tail.next = ListNode(digit)
            tail = tail.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
''',
      [([[2, 4, 3], [5, 6, 4]], [7, 0, 8]), ([[0], [0]], [0]),
       ([[9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]], [8, 9, 9, 9, 0, 0, 0, 1]), ([[1], [9, 9]], [0, 0, 1]),
       ([[5], [5]], [0, 1]), ([[1, 8], [0]], [1, 8]), ([[9, 9], [1]], [0, 0, 1])],
      arg_types=["list_node", "list_node"], return_type="list_node",
      gen=lambda rng: [[_digits(rng, rng.randint(1, 12)), _digits(rng, rng.randint(1, 12))] for _ in range(4)]
      + [[_digits(rng, 3000), _digits(rng, 2900)]] + [[[9] * 3000, [1]]],
      small=lambda rng: [_digits(rng, rng.randint(1, 6)), _digits(rng, rng.randint(1, 6))],
      brute=r'''
class Solution:
    def addTwoNumbers(self, l1, l2):
        def num(h):
            digits = []
            while h:
                digits.append(str(h.val))
                h = h.next
            return int("".join(reversed(digits)))
        total = str(num(l1) + num(l2))
        out = None
        for ch in total:
            out = ListNode(int(ch), out)
        return out
'''),

    P(42, "Find the Duplicate Number", "Medium", "findDuplicate",
      r'''
`nums` contains `n + 1` integers, each in the range `[1, n]`. Exactly one value is repeated (it may appear more than twice); every other value appears once.

Return the repeated value. You must not modify `nums`, and you should use only O(1) extra space.

## Examples

```
Input:  nums = [1, 2, 3, 2, 2]
Output: 2

Input:  nums = [1, 2, 3, 4, 4]
Output: 4
```

## Constraints

- `1 <= n <= 10000`
- `len(nums) == n + 1`

## Hints

- Treat `nums[i]` as a "next" pointer from index `i`. The duplicate is where two paths enter the same cycle.
- Floyd's tortoise and hare finds the cycle entrance.
''',
      r'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        pass
''',
      r'''
class Solution:
    def findDuplicate(self, nums):
        slow = fast = 0
        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while slow != slow2:
            slow, slow2 = nums[slow], nums[slow2]
        return slow
''',
      [([[1, 2, 3, 2, 2]], 2), ([[1, 2, 3, 4, 4]], 4), ([[1, 3, 4, 2, 2]], 2), ([[3, 1, 3, 4, 2]], 3),
       ([[1, 1]], 1), ([[2, 2, 2]], 2), ([[1, 4, 4, 2, 4]], 4)],
      gen=_dup_gen, small=_dup_small,
      brute=r'''
from collections import Counter


class Solution:
    def findDuplicate(self, nums):
        return Counter(nums).most_common(1)[0][0]
'''),

    P(43, "LRU Cache", "Medium", "LRUCache",
      r'''
Design a cache that keeps at most `capacity` entries and evicts the least recently used one when it is full.

Implement the class `LRUCache`:

- `LRUCache(capacity)` creates a cache that holds up to `capacity` keys.
- `get(key)` returns the value for `key`, or `-1` if it is not present. A successful `get` makes `key` the most recently used.
- `put(key, value)` inserts or updates `key`, making it the most recently used. If this pushes the size above `capacity`, remove the least recently used key.

Both `get` and `put` must run in O(1) average time.

## Examples

```
LRUCache(2)
put(1, 1); put(2, 2)
get(1)      -> 1
put(3, 3)           # evicts key 2
get(2)      -> -1
put(4, 4)           # evicts key 1
get(1)      -> -1
get(3)      -> 3
get(4)      -> 4
```

## Constraints

- `1 <= capacity <= 100`
- `0 <= key <= 1000`, `0 <= value <= 10^5`
- At most `10000` calls are made.

## Hints

- A hash map gives O(1) lookup; a doubly linked list gives O(1) reordering and eviction.
''',
      r'''
class LRUCache:

    def __init__(self, capacity: int):
        pass

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        pass
''',
      r'''
from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.data = OrderedDict()

    def get(self, key):
        if key not in self.data:
            return -1
        self.data.move_to_end(key)
        return self.data[key]

    def put(self, key, value):
        self.data[key] = value
        self.data.move_to_end(key)
        if len(self.data) > self.cap:
            self.data.popitem(last=False)
''',
      [([["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
         [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]],
        [None, None, None, 1, None, -1, None, -1, 3, 4]),
       ([["LRUCache", "put", "get", "put", "get", "get"], [[1], [2, 1], [2], [3, 2], [2], [3]]],
        [None, None, 1, None, -1, 2]),
       ([["LRUCache", "put", "put", "put", "put", "get", "get", "get"], [[2], [1, 1], [2, 2], [1, 10], [3, 3], [2], [1], [3]]],
        [None, None, None, None, None, -1, 10, 3]),
       ([["LRUCache", "get", "put", "get"], [[3], [9], [9, 5], [9]]], [None, -1, None, 5])],
      design="LRUCache",
      gen=lambda rng: [_lru(rng, 2, 30, 4), _lru(rng, 3, 80, 6), _lru(rng, 5, 200, 12), _lru(rng, 100, 6000, 150)],
      small=lambda rng: _lru(rng, rng.randint(1, 3), rng.randint(1, 14), 4),
      brute=r'''
class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.items = []

    def get(self, key):
        for i, (k, v) in enumerate(self.items):
            if k == key:
                self.items.append(self.items.pop(i))
                return v
        return -1

    def put(self, key, value):
        self.items = [(k, v) for k, v in self.items if k != key]
        self.items.append((key, value))
        if len(self.items) > self.cap:
            self.items.pop(0)
'''),

    P(44, "Merge k Sorted Lists", "Hard", "mergeKLists",
      r'''
You are given a list `lists` of `k` linked lists, each sorted in ascending order. Merge them all into one sorted linked list and return its head.

## Examples

```
Input:  lists = [[1, 2, 4], [1, 3, 5], [3, 6]]
Output: [1, 1, 2, 3, 3, 4, 5, 6]

Input:  lists = []
Output: []
```

## Constraints

- `0 <= k <= 100`
- `0 <= length of each list <= 100`, and the total number of nodes is at most `10000`
- `-1000 <= node.val <= 1000`

## Hints

- A min-heap holding the current head of every list gives the next smallest node in O(log k).
- Alternatively, merge the lists pairwise, like merge sort.
''',
      LIST_HDR + r'''
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pass
''',
      r'''
import heapq


class Solution:
    def mergeKLists(self, lists):
        heap = [(node.val, i, node) for i, node in enumerate(lists) if node]
        heapq.heapify(heap)
        dummy = tail = ListNode()
        while heap:
            _, i, node = heapq.heappop(heap)
            tail.next = node
            tail = node
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        return dummy.next
''',
      [([[[1, 2, 4], [1, 3, 5], [3, 6]]], [1, 1, 2, 3, 3, 4, 5, 6]), ([[]], []), ([[[]]], []), ([[[], []]], []),
       ([[[1], [0]]], [0, 1]), ([[[2], [], [1]]], [1, 2]), ([[[1, 1], [1, 1]]], [1, 1, 1, 1]),
       ([[[-3, -1], [-2, 0]]], [-3, -2, -1, 0])],
      arg_types=["list_of_list_node"], return_type="list_node",
      gen=lambda rng: [_klists(rng, 3, 4), _klists(rng, 6, 6), _klists(rng, 20, 10),
                       [[_sorted(rng, 100, -1000, 1000) for _ in range(100)]]],
      small=lambda rng: _klists(rng, rng.randint(0, 5), 5),
      brute=r'''
class Solution:
    def mergeKLists(self, lists):
        vals = []
        for head in lists:
            while head:
                vals.append(head.val)
                head = head.next
        out = None
        for v in sorted(vals, reverse=True):
            out = ListNode(v, out)
        return out
'''),

    P(45, "Reverse Nodes in k-Group", "Hard", "reverseKGroup",
      r'''
Given the head of a linked list and an integer `k`, reverse the nodes of the list `k` at a time and return the new head.

If the number of remaining nodes at the end is less than `k`, leave those nodes as they are. You may only change node pointers, not node values.

## Examples

```
Input:  head = [1, 2, 3, 4, 5], k = 2
Output: [2, 1, 4, 3, 5]

Input:  head = [1, 2, 3, 4, 5], k = 3
Output: [3, 2, 1, 4, 5]
```

## Constraints

- `1 <= k <= number of nodes <= 5000`
- `0 <= node.val <= 1000`

## Hints

- Check that `k` nodes remain before reversing a group, then reconnect the reversed group to the rest.
''',
      LIST_HDR + r'''
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        pass
''',
      r'''
class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0, head)
        group_prev = dummy
        while True:
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            group_next = kth.next
            prev, cur = group_next, group_prev.next
            while cur is not group_next:
                cur.next, prev, cur = prev, cur, cur.next
            group_prev.next, group_prev = kth, group_prev.next
''',
      [([[1, 2, 3, 4, 5], 2], [2, 1, 4, 3, 5]), ([[1, 2, 3, 4, 5], 3], [3, 2, 1, 4, 5]), ([[1], 1], [1]),
       ([[1, 2], 2], [2, 1]), ([[1, 2, 3, 4], 4], [4, 3, 2, 1]), ([[1, 2, 3], 4], [1, 2, 3]),
       ([[1, 2, 3, 4, 5, 6], 3], [3, 2, 1, 6, 5, 4]), ([[1, 2, 3, 4, 5, 6, 7], 3], [3, 2, 1, 6, 5, 4, 7]),
       ([[1, 2, 3], 1], [1, 2, 3])],
      arg_types=["list_node", "plain"], return_type="list_node",
      gen=lambda rng: [[_vals(rng, n, 0, 99), rng.randint(1, n)] for n in (4, 9, 15)]
      + [[_vals(rng, 5000, 0, 1000), 2], [_vals(rng, 5000, 0, 1000), 7], [_vals(rng, 5000, 0, 1000), 5000]],
      small=lambda rng: (lambda n: [_vals(rng, n, 0, 20), rng.randint(1, n)])(rng.randint(1, 9)),
      brute=r'''
class Solution:
    def reverseKGroup(self, head, k):
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        out = []
        for i in range(0, len(vals), k):
            chunk = vals[i:i + k]
            out += chunk[::-1] if len(chunk) == k else chunk
        node = None
        for v in reversed(out):
            node = ListNode(v, node)
        return node
'''),
]


def _digits(rng, n):
    d = [rng.randint(0, 9) for _ in range(n)]
    if n > 1 and d[-1] == 0:
        d[-1] = rng.randint(1, 9)
    return d

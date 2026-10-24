### Approach

You need a lookup by key and a way to know which key was used least recently, both in constant time. Python's `OrderedDict` keeps keys in order and can move one to the end in O(1). Treat the end as most recently used. `get` and `put` both move the key to the end, and when the size goes over capacity, `popitem(last=False)` removes the oldest key.

### Complexity

- Time: O(1) per operation.
- Space: O(capacity).

### Alternatives

Without `OrderedDict`, the classic design is a dictionary plus a doubly linked list. The dictionary points at list nodes, and moving a node to the front or removing the tail is O(1).

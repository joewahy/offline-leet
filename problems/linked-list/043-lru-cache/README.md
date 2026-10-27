# 43. LRU Cache (Medium)

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

- `1 <= capacity <= 10^5`
- `0 <= key <= 10^5`, `0 <= value <= 10^5`
- At most `10^5` calls are made.

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. You need O(1) lookup by key and O(1) updates to the usage order. One structure alone cannot do both.
2. Combine a hash map (key to node) with a doubly linked list ordered from least to most recently used.
3. On `get` or `put`, move the node to the most-recent end. When the size exceeds the capacity, remove the node at the least-recent end and delete its key from the map. Dummy head and tail nodes avoid edge cases. (In Python, `OrderedDict` with `move_to_end` does the same job.)

</details>

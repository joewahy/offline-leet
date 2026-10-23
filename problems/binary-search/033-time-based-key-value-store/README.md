# 33. Time Based Key-Value Store (Medium)

Design a key-value store that remembers every value a key has ever had, together with the time it was set.

Implement the class `TimeMap`:

- `TimeMap()` creates an empty store.
- `set(key, value, timestamp)` stores `value` for `key` at `timestamp`.
- `get(key, timestamp)` returns the value that was set for `key` at the largest timestamp that is less than or equal to `timestamp`. If there is no such value, return `""`.

For a given key, `set` is always called with strictly increasing timestamps.

## Examples

```
set("alice", "happy", 1)
get("alice", 1)   -> "happy"
get("alice", 2)   -> "happy"
set("alice", "sad", 3)
get("alice", 3)   -> "sad"
get("alice", 4)   -> "sad"
```

## Constraints

- `1 <= len(key), len(value) <= 100`
- `1 <= timestamp <= 10^7`
- At most `10000` calls are made.

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. For each key, the values come with increasing timestamps. What does that let you do when looking one up?
2. Store a sorted list of timestamps (and the matching values) per key, and use binary search in `get`.
3. In `get`, find the rightmost timestamp `<= t` with `bisect_right(times, t) - 1`. If the index is negative, return an empty string. `set` just appends.

</details>

# 61. Kth Largest Element in a Stream (Easy)

Design a class that tracks the `k`-th largest value in a stream of integers. It is the `k`-th largest in sorted order, not the `k`-th distinct value.

Implement `KthLargest`:

- `KthLargest(k, nums)` starts with the integer `k` and the initial stream `nums`.
- `add(val)` appends `val` to the stream and returns the `k`-th largest value seen so far.

## Examples

```
KthLargest(3, [1, 2, 3, 3])
add(3)   -> 3
add(5)   -> 3
add(6)   -> 3
add(7)   -> 5
add(8)   -> 6
```

## Constraints

- `1 <= k <= 1000`
- `0 <= len(nums) <= 1000`, and the stream always has at least `k` values when `add` is called
- `-1000 <= val <= 1000`
- At most `1000` calls to `add`.

## Hints

- A min-heap of size `k` keeps the `k` largest values; its smallest element is the answer.

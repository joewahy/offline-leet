### Approach

Instead of searching the piles, search the answer. The eating speed lies between 1 and the biggest pile. A speed `s` takes `sum(ceil(p / s))` hours, and a faster speed never takes longer, so the question "is this speed fast enough?" flips from no to yes exactly once. Binary search for that point.

`-(-p // mid)` is a way to write `ceil(p / mid)` using only integers.

### Complexity

- Time: O(n log m), where `m` is the largest pile. There are log m rounds and each one adds up `n` piles.
- Space: O(1).

### Alternatives

Trying every speed from 1 upward is O(n * m), which is far too slow when piles are as large as a billion.

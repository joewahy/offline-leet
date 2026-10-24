### Approach

Splitting into two equal halves is possible exactly when some subset adds up to half the total. If the total is odd, it is impossible. Otherwise find which sums can be made. This reference stores them as the bits of one big integer: bit `s` is set if sum `s` is reachable. Adding a number `x` is a single shift-and-or, `reach |= reach << x`. The answer is whether the bit at `total // 2` is set.

### Complexity

- Time: O(n * sum) bit operations, but the shift works on many bits at a time, so it is fast in practice.
- Space: O(sum) bits.

### Alternatives

The usual version uses a boolean array over sums and loops from high to low so each number is used once.

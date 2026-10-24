### Approach

Exponentiation by squaring. Instead of multiplying `x` by itself `n` times, look at the bits of `n`. Keep squaring `x` so it takes the values `x`, `x^2`, `x^4`, and so on. Whenever the current bit of `n` is 1, multiply that power into the result. A negative exponent is handled by inverting `x` and using `-n`.

### Complexity

- Time: O(log n), one step per bit of `n`.
- Space: O(1).

### Watch out

A loop that multiplies `n` times takes billions of steps for `n` near 2^31 and times out.

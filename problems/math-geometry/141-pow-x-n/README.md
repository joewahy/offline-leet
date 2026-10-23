# 141. Pow(x, n) (Medium)

Implement `pow(x, n)`: return `x` raised to the power `n`. `x` is a floating-point number and `n` is an integer, which may be negative. Your answer is accepted if it is within `1e-5` of the exact value.

Do not use `**`, `pow`, or `math.pow`. Aim for O(log n) multiplications.

## Examples

```
Input:  x = 2.0, n = 10
Output: 1024.0

Input:  x = 2.0, n = -2
Output: 0.25
```

## Constraints

- `-100.0 < x < 100.0`
- `-2^31 <= n <= 2^31 - 1`
- `x` is not `0` when `n` is negative; the result is between `-10^4` and `10^4`.

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Multiplying `x` by itself `n` times is too slow for large `n`. Can you halve the work at each step?
2. Use `x^n = (x^(n/2))^2`, with one extra factor of `x` when `n` is odd.
3. Iterate over the bits of `n`: square `x` at each step, and multiply the result by `x` when the current bit is 1. For negative `n`, use `1 / x` and `-n`.

</details>

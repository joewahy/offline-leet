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

## Hints

- Square the base and halve the exponent: `x^n = (x^2)^(n/2)`. Handle odd `n` with one extra multiplication, and negate `n` for the reciprocal.

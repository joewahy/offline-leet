# 149. Sum of Two Integers (Medium)

Return the sum of two integers `a` and `b` without using the operators `+` and `-`.

(The tests cannot enforce this rule, but the point of the problem is to build addition out of bit operations.)

## Examples

```
Input:  a = 1, b = 2
Output: 3

Input:  a = -2, b = -3
Output: -5
```

## Constraints

- `-1000 <= a, b <= 1000`

## Hints

- `a ^ b` adds without carrying, and `(a & b) << 1` is the carry. Repeat until there is no carry.
- In Python, integers are unbounded, so mask to 32 bits and convert back to a signed value at the end.

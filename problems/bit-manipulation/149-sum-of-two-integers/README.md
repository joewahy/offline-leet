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

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Think about how you add in binary. Which operation gives the sum without carries, and which gives the carries?
2. XOR adds without carrying. AND, shifted left by one, gives the carry.
3. Repeat `a, b = a ^ b, (a & b) << 1` until `b` is 0. In Python, integers are unbounded, so mask to 32 bits (`& 0xFFFFFFFF`) at each step, and convert back to a negative number at the end if the 32nd bit is set.

</details>

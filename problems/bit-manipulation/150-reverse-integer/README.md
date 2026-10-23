# 150. Reverse Integer (Medium)

Given a signed 32-bit integer `x`, return `x` with its decimal digits reversed (keeping the sign). If the reversed value does not fit in a signed 32-bit integer (outside `[-2^31, 2^31 - 1]`), return `0`.

## Examples

```
Input:  x = 123
Output: 321

Input:  x = -123
Output: -321

Input:  x = 1534236469
Output: 0          # the reverse overflows
```

## Constraints

- `-2^31 <= x <= 2^31 - 1`

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Peel off the last digit with `% 10` and add it to the end of a new number.
2. Handle the sign separately: work with the absolute value, then put the sign back.
3. Build `rev = rev * 10 + digit` while dividing the input by 10. In Python nothing overflows by itself, so check at the end whether the result is within `[-2^31, 2^31 - 1]` and return `0` if it is not.

</details>

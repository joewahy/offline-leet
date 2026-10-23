# 105. Decode Ways (Medium)

A message made of capital letters is encoded as digits using `A -> "1"`, `B -> "2"`, ..., `Z -> "26"`. To decode a digit string, split it into groups that are each a valid code (`"1"` to `"26"`, with no leading zero), and map each group back to a letter.

For example `"11106"` can be decoded as `"AAJF"` (`1 1 10 6`) or `"KJF"` (`11 10 6`), but not as `1 1 1 06`, because `"06"` is not valid.

Return the number of different ways to decode `s`. If there are none, return `0`.

## Examples

```
Input:  s = "12"
Output: 2          # "AB" or "L"

Input:  s = "06"
Output: 0
```

## Constraints

- `1 <= len(s) <= 45`
- `s` contains only digits and may start with `0`.
- The answer fits in a 32-bit integer.

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. At each position you may read one digit or two. Which choices are valid?
2. One digit is valid if it is not `0`. Two digits are valid if they form a number from 10 to 26.
3. Let `ways(i)` be the count for the suffix starting at `i`, with `ways(n) = 1`. If `s[i] != '0'`, then `ways(i) = ways(i+1)`, plus `ways(i+2)` when `s[i:i+2] <= '26'`. Otherwise `ways(i) = 0`.

</details>

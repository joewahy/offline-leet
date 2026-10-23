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

## Hints

- At each position you can use one digit (if it is not `0`) or two digits (if they form 10 to 26). Add up the ways for the rest of the string.

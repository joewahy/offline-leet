# 142. Multiply Strings (Medium)

Two non-negative integers are given as decimal strings `num1` and `num2`. Return their product as a string.

You may not use a big-integer library or convert the input strings directly to integers; do the multiplication digit by digit, as on paper.

## Examples

```
Input:  num1 = "3", num2 = "4"
Output: "12"

Input:  num1 = "123", num2 = "456"
Output: "56088"
```

## Constraints

- `1 <= len(num1), len(num2) <= 200`
- Digits only; no leading zeros except the number `0` itself.

## Hints

- The product has at most `len(num1) + len(num2)` digits. Digit `i` of one number times digit `j` of the other lands at position `i + j`.

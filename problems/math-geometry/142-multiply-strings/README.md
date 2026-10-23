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

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Do it the way you would on paper, one digit at a time.
2. The product of digit `i` of `num1` and digit `j` of `num2` contributes to position `i + j + 1` of the result (with a carry into `i + j`).
3. Use a result array of length `len(num1) + len(num2)`. Loop from the right, add the digit product to `res[i + j + 1]`, then carry `total // 10` into `res[i + j]`. Strip leading zeros at the end, and handle `'0'` specially.

</details>

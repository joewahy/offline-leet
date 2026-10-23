# 75. Letter Combinations of a Phone Number (Medium)

Each digit from `2` to `9` on a phone keypad maps to letters: `2 -> abc`, `3 -> def`, `4 -> ghi`, `5 -> jkl`, `6 -> mno`, `7 -> pqrs`, `8 -> tuv`, `9 -> wxyz`.

Given a string `digits`, return every letter combination it could spell, in any order. If `digits` is empty, return an empty list.

## Examples

```
Input:  digits = "34"
Output: ["dg", "dh", "di", "eg", "eh", "ei", "fg", "fh", "fi"]

Input:  digits = ""
Output: []
```

## Constraints

- `0 <= len(digits) <= 4`
- Each digit is between `'2'` and `'9'`.

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. Each digit contributes exactly one letter. How many choices does each digit give?
2. Store the letters for each digit in a map, and build the combinations digit by digit.
3. Iterative: start with `['']` and, for each digit, replace the list by every existing prefix plus each letter of that digit. Return `[]` for empty input.

</details>

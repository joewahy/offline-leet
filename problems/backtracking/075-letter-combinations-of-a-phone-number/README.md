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

## Hints

- Build one letter per digit, trying every letter that digit maps to.

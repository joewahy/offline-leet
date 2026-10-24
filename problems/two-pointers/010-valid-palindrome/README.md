# 10. Valid Palindrome (Easy)

Given a string `s`, decide whether it reads the same forwards and backwards after you throw away every character that is not a letter or digit and ignore upper/lower case.

Return `True` if it is a palindrome under those rules, otherwise `False`.

## Examples

```
Input:  s = "Was it a car or a cat I saw?"
Output: True

Input:  s = "tab a cat"
Output: False
```

## Constraints

- `1 <= len(s) <= 10^5`
- `s` contains printable ASCII characters.

## Hints

- Use one pointer at each end and move them towards each other, skipping characters that do not count.
- `str.isalnum()` tells you whether a character counts.

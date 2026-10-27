# 129. Valid Parenthesis String (Medium)

The string `s` contains only `(`, `)` and `*`. The `*` is a wildcard: it may be treated as `(`, as `)`, or as an empty string.

Return `True` if `s` can be made a valid parentheses string, otherwise `False`. A valid string has every `(` matched by a later `)` and every `)` matched by an earlier `(`.

## Examples

```
Input:  s = "((**))"
Output: True

Input:  s = "(((*)"
Output: False
```

## Constraints

- `1 <= len(s) <= 10^5`
- Each character is `(`, `)` or `*`.

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. A `*` can be three things, so the number of unmatched `(` is not one value but a range.
2. Track the smallest and the largest possible count of open parentheses as you scan.
3. `(` adds 1 to both, `)` subtracts 1 from both, and `*` subtracts 1 from the lower and adds 1 to the upper. If the upper bound goes below 0, return false. Clamp the lower bound at 0. At the end, the lower bound must be 0.

</details>

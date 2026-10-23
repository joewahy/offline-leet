# 139. Happy Number (Easy)

Start with a positive integer `n`. Repeatedly replace it by the sum of the squares of its digits. If this process eventually reaches `1`, `n` is happy. If it falls into a loop that never reaches `1`, it is not.

Return `True` if `n` is a happy number, otherwise `False`.

## Examples

```
Input:  n = 100
Output: True       # 1^2 + 0^2 + 0^2 = 1

Input:  n = 101
Output: False
```

## Constraints

- `1 <= n <= 2^31 - 1`

## Hints

- Remember the numbers you have already seen; seeing one twice means a cycle.
- Floyd's tortoise and hare also detects the cycle without extra memory.

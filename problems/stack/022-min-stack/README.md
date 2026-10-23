# 22. Min Stack (Medium)

Design a stack that supports the usual operations and can also report its smallest element, all in O(1) time.

Implement the class `MinStack`:

- `MinStack()` creates an empty stack.
- `push(val)` pushes `val`.
- `pop()` removes the top element.
- `top()` returns the top element.
- `getMin()` returns the smallest element currently in the stack.

`pop`, `top` and `getMin` are only called when the stack is not empty.

## Examples

```
MinStack(); push(1); push(2); push(0)
getMin()  -> 0
pop()
top()     -> 2
getMin()  -> 1
```

## Constraints

- `-2^31 <= val <= 2^31 - 1`
- At most `10000` calls are made.

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. `getMin` must be O(1), so you cannot scan the stack. What extra information could each stack entry carry?
2. Along with each value, store the minimum of the stack at the moment it was pushed.
3. Push `(val, min(val, previous_min))`. Then `getMin` reads the top entry's second item, and `pop` automatically restores the earlier minimum.

</details>

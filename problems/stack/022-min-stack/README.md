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

## Hints

- Store with each element the minimum of everything beneath it (and itself).

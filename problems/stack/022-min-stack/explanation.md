### Approach

Store each value together with the minimum of everything at or below it in the stack. When you push, the new minimum is the smaller of the new value and the previous top's minimum. Popping removes the pair, so the previous minimum is back automatically, and `getMin` just reads the top.

### Complexity

- Time: O(1) per operation.
- Space: O(n), one extra number per element.

### Alternatives

Calling `min` over the stack each time is O(n) per `getMin` and times out on long runs of operations.

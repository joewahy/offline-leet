### Approach

A window can become all one letter if the number of characters that are not its most common letter is at most `k`. So grow the window to the right, counting letters. While `window length - highest count > k`, the window needs too many replacements, so shrink it from the left. The longest window that was valid is the answer.

### Complexity

- Time: O(n). The `max` over the counts looks at at most 26 letters, which is a constant.
- Space: O(1), at most 26 counts.

### Alternatives

You can avoid recomputing the maximum by keeping a running `max_count` that never decreases. It can be stale after the window shrinks, but a stale value can never make a window look better than the true best, so the answer stays correct.

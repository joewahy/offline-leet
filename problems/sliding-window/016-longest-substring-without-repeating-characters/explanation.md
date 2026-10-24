### Approach

Keep a window `[left, right]` that never contains a repeated character. Store the last index where each character appeared. When the next character was last seen inside the current window, jump `left` to just after that spot. Then record the character's new index and update the best length.

Jumping `left` in one move is what keeps the window valid without shrinking it one step at a time.

### Complexity

- Time: O(n), `right` moves once per character and `left` never moves backward.
- Space: O(alphabet size), at most one entry per distinct character.

### Watch out

The check `last[ch] >= left` matters. A character seen before the window started does not count as a repeat.

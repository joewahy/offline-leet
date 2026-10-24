### Approach

Work through the list in groups of `k`. For each group, first check that `k` nodes really exist (walk `k` steps from the node before the group). If not, stop and leave the rest alone. Otherwise reverse just that group in place, reconnecting it to the node before and the node after, and move on to the next group.

Reversing starts with `prev` set to the node after the group, so the last node of the reversed group already points to the rest of the list.

### Complexity

- Time: O(n). Each node is visited a couple of times.
- Space: O(1).

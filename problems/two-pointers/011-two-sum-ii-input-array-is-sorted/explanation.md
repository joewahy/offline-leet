### Approach

Because the list is sorted, two pointers can find the pair without a dictionary. Start one at each end. If the sum is too small, only moving the left pointer right can raise it. If it is too big, only moving the right pointer left can lower it. Each step rules out one element for good.

The answer uses 1-based positions, so add 1 to each index.

### Complexity

- Time: O(n), the pointers only move toward each other.
- Space: O(1), which is what the problem asks for. The hash map from Two Sum would use O(n).

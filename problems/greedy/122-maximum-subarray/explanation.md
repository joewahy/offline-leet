### Approach

Kadane's algorithm. Track the best sum of a subarray that ends at the current element. At each number, either start fresh from it, or extend the previous subarray, whichever is larger. A previous sum that is negative can only hurt, which is why starting fresh wins in that case. The answer is the best value seen across all positions.

### Complexity

- Time: O(n).
- Space: O(1).

### Watch out

Start from `nums[0]`, not 0, so an all-negative list returns its largest (least negative) element.

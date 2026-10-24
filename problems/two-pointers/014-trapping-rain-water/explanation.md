### Approach

The water above a bar is the lower of the tallest bar to its left and the tallest to its right, minus the bar's own height. Two pointers get this without storing prefix maximums.

Compare the heights at the two ends. The smaller side is the limiting one, because there is a bar at least that tall on the other side. So process that side: update its running maximum, add the water above the bar (maximum minus height), and move that pointer inward.

### Complexity

- Time: O(n), one sweep.
- Space: O(1). The simpler version builds two arrays of prefix and suffix maximums, which is also O(n) time but O(n) space.

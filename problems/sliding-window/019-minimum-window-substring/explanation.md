### Approach

Grow a window to the right until it holds every character `t` needs, then shrink it from the left as far as it stays valid. The shortest valid window seen along the way is the answer.

The reference keeps one `Counter` of what is still needed. A positive count means that character is still missing. `missing` tracks how many characters of `t` are not yet covered, so checking validity is a single comparison with 0 instead of scanning the counter.

### Complexity

- Time: O(n + m). Both pointers only move forward, so each character is added and removed at most once.
- Space: O(alphabet size) for the counter.

### Watch out

Extra copies of a letter push its count below zero, which is how the code knows it can drop one from the left without breaking the window.

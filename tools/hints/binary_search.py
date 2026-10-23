HINTS = {
    29: [
        "Because each row starts after the previous row ends, the whole matrix is in sorted order when read row by row.",
        "Treat it as one sorted list of `rows * cols` items and binary search over the indices `0 .. rows * cols - 1`.",
        "Convert a flat index `mid` to a cell with `row = mid // cols` and `col = mid % cols`. That gives O(log(m * n)) time.",
    ],
    30: [
        "If Koko can finish at speed `k`, can she also finish at any faster speed? What does that tell you about the answer?",
        "Yes, so feasibility is monotonic: binary search on the speed between 1 and `max(piles)`.",
        "To test a speed `k`, add up `ceil(pile / k)` hours over all piles and compare the total with `h`. Use `(pile + k - 1) // k` for the ceiling. Find the smallest speed that works.",
    ],
    31: [
        "The minimum is the point where the order drops. Which half of the array contains that drop?",
        "Compare `nums[mid]` with `nums[right]`. If it is larger, the drop (and the minimum) is to the right of `mid`.",
        "If `nums[mid] > nums[right]` set `left = mid + 1`, otherwise set `right = mid` (keep `mid`, as it may be the minimum). Stop when `left == right`.",
    ],
    32: [
        "After splitting at the middle, at least one half is still in normal sorted order. How can you tell which?",
        "Compare `nums[left]` with `nums[mid]`: if `nums[left] <= nums[mid]`, the left half is sorted; otherwise the right half is.",
        "Check whether `target` lies inside the sorted half's range. If yes, search that half; if not, search the other half. Repeat until found, in O(log n).",
    ],
    33: [
        "For each key, the values come with increasing timestamps. What does that let you do when looking one up?",
        "Store a sorted list of timestamps (and the matching values) per key, and use binary search in `get`.",
        "In `get`, find the rightmost timestamp `<= t` with `bisect_right(times, t) - 1`. If the index is negative, return an empty string. `set` just appends.",
    ],
    34: [
        "Merging both arrays and taking the middle is O(m + n). To do better you cannot look at every element.",
        "Binary search how many elements of the smaller array belong in the left half of the merged order. The rest of the left half comes from the other array.",
        "A split is right when `maxLeftA <= minRightB` and `maxLeftB <= minRightA` (use infinity for empty sides). Then the median comes from those four values: the larger left value, and for an even total also the smaller right value.",
    ],
}

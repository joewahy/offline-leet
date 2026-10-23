HINTS = {
    122: [
        "If the sum of a prefix is negative, can it help any later subarray?",
        "No. A negative running sum should be thrown away and a new subarray started.",
        "Keep `cur = max(x, cur + x)` and the best `cur` seen. This is Kadane's algorithm, O(n) time and O(1) space.",
    ],
    123: [
        "You do not have to find the exact jumps, only whether the end is reachable.",
        "Track the farthest index you can reach so far.",
        "Scan left to right. If your index is beyond the farthest reach, return false. Otherwise update `reach = max(reach, i + nums[i])`. If you finish the scan, return true.",
    ],
    124: [
        "Think of each jump as moving to a new 'level' of indices, like in a BFS.",
        "From the current level (the indices reachable with `j` jumps), find the farthest index you can reach with one more jump.",
        "Track `end` (the end of the current level) and `far`. When you reach `i == end`, you must jump: increment the count and set `end = far`. Stop before the last index.",
    ],
    125: [
        "If the total gas is less than the total cost, can any start work?",
        "No, so return `-1`. Otherwise a start exists. If the tank goes negative going from station `a` to `b`, no station between them can be the start.",
        "Scan once keeping `tank += gas[i] - cost[i]`. When `tank < 0`, set the candidate start to `i + 1` and reset `tank = 0`. After the scan (and the total check), the candidate is the answer.",
    ],
    126: [
        "If the number of cards is not a multiple of `groupSize`, it is impossible. Otherwise, which card must start a group?",
        "The smallest remaining card must start a group, because nothing smaller could come before it.",
        "Count the cards. Go through the values in increasing order: for a value with count `c`, you need `c` copies of each of the next `groupSize - 1` values too. Subtract them, and fail if any is short.",
    ],
    127: [
        "Merging takes the maximum at each position, so it can only increase values. Which triplets can never be used?",
        "Any triplet with a value larger than the target in some position can never be used, because the maximum would overshoot.",
        "Among the usable triplets, take the position-wise maximum. If it equals the target, return true. Equivalently, check that each target position is matched by some usable triplet.",
    ],
    128: [
        "If a letter appears in a part, that part must reach at least the letter's last occurrence.",
        "Record the last index of every letter.",
        "Scan the string, keeping `end = max(end, last[c])`. When the index `i` reaches `end`, close the part, record its length, and start the next one.",
    ],
    129: [
        "A `*` can be three things, so the number of unmatched `(` is not one value but a range.",
        "Track the smallest and the largest possible count of open parentheses as you scan.",
        "`(` adds 1 to both, `)` subtracts 1 from both, and `*` subtracts 1 from the lower and adds 1 to the upper. If the upper bound goes below 0, return false. Clamp the lower bound at 0. At the end, the lower bound must be 0.",
    ],
}

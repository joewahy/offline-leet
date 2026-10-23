HINTS = {
    130: [
        "The list is sorted. Relative to the new interval, each interval falls into one of three groups: before it, overlapping it, or after it.",
        "Copy the intervals that end before the new one starts, merge all the ones that overlap it, then copy the rest.",
        "While `intervals[i][1] < new[0]`, copy. While `intervals[i][0] <= new[1]`, set `new = [min of starts, max of ends]`. Append the merged interval, then copy the remaining intervals.",
    ],
    131: [
        "Overlaps are hard to see when the intervals are in random order. What if they were sorted?",
        "Sort by start. Then only the previous merged interval can overlap the next one.",
        "Keep a result list. For each interval, if its start is `<=` the last result's end, set that end to the larger of the two ends; otherwise append a new interval.",
    ],
    132: [
        "When two intervals overlap, you must remove one. Which one is the better choice to keep?",
        "Keep the one that ends earlier, since it leaves the most room for the rest.",
        "Sort by end time. Track the end of the last kept interval. For each interval, if its start is `>=` that end, keep it; otherwise count one removal.",
    ],
    134: [
        "The number of rooms needed is the largest number of meetings running at the same moment.",
        "Look at the start and end events in time order. A start adds a meeting, an end removes one.",
        "Sort the start times and the end times separately. Sweep through the starts: while the earliest end is `<=` the current start, free a room. Then use a room. Track the maximum in use. A min-heap of end times also works.",
    ],
    135: [
        "Checking every interval for every query is too slow. What if you handled the queries in sorted order?",
        "Sort the intervals by start and the queries in ascending order, and sweep through them together.",
        "For each query, push into a min-heap `(size, end)` every interval whose start is `<= query`. Pop the top while its end is `< query`. The top's size is the answer, or `-1` if the heap is empty. Remember the original order of the queries.",
    ],
}

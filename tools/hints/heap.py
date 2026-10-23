HINTS = {
    63: [
        "You do not need the actual distances, only their order. Which values compare the same way as distances?",
        "Compare squared distances `x*x + y*y` and avoid the square root. Then pick the `k` smallest.",
        "Sorting by squared distance is O(n log n). A max-heap of size `k` is O(n log k), and `heapq.nsmallest(k, points, key=...)` does it for you.",
    ],
    64: [
        "Sorting the whole array works. Do you need the entire order, or just the top `k`?",
        "Keep a min-heap of size `k`. After processing every number, its smallest element is the `k`-th largest.",
        "Push each number; if the heap grows beyond `k`, pop the smallest. That is O(n log k). Quickselect gives O(n) on average.",
    ],
    65: [
        "The task that appears most often is the bottleneck, because its copies need gaps between them.",
        "Lay out the most frequent task with `n` slots between its copies. Other tasks fill those gaps, and idle time remains only if the gaps cannot be filled.",
        "With `top` = highest count and `ties` = how many tasks have that count, the answer is `max(len(tasks), (top - 1) * (n + 1) + ties)`. Or simulate with a max-heap and a cooldown queue.",
    ],
    66: [
        "The feed needs the 10 most recent tweets across several users. What gives you 'most recent'?",
        "Give every tweet a global timestamp (an incrementing counter), store each user's tweets in order, and keep a set of followees per user.",
        "For `getNewsFeed`, gather the latest 10 tweets of the user and of each followee, and take the 10 with the largest timestamps (a heap or `heapq.nlargest`). Include the user's own tweets even though they do not follow themselves.",
    ],
    67: [
        "The median sits between the smaller half and the larger half of the numbers. You only need the boundary of each half.",
        "Keep the smaller half in a max-heap and the larger half in a min-heap, so each heap's top is next to the median.",
        "Insert into one heap, then move the top across so every element of the small half is `<=` every element of the large half. Keep the sizes equal or differing by 1. The median is the top of the bigger heap, or the average of both tops. Python's `heapq` is a min-heap, so store negatives for the max-heap.",
    ],
}

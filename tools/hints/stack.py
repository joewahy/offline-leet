HINTS = {
    22: [
        "`getMin` must be O(1), so you cannot scan the stack. What extra information could each stack entry carry?",
        "Along with each value, store the minimum of the stack at the moment it was pushed.",
        "Push `(val, min(val, previous_min))`. Then `getMin` reads the top entry's second item, and `pop` automatically restores the earlier minimum.",
    ],
    23: [
        "Operands wait until their operator arrives. Which data structure holds things that are waiting?",
        "Push numbers onto a stack. On an operator, pop the top two values, apply it, and push the result.",
        "Pop `b` first, then `a`, and compute `a op b` (the order matters for `-` and `/`). Division truncates toward zero, so use `int(a / b)` rather than `//`.",
    ],
    24: [
        "Build the string one character at a time. At each step, which characters are allowed?",
        "You may add `(` if fewer than `n` have been used, and `)` if the number of `)` is less than the number of `(`.",
        "Use backtracking with counts `opens` and `closes`. When the string reaches length `2n`, record it. Every string you reach is valid, so no work is wasted.",
    ],
    25: [
        "For each day you want the next warmer day. Checking every later day is O(n^2). What is waiting for an answer at any moment?",
        "Keep a stack of days that have not found a warmer day yet. Their temperatures are non-increasing from bottom to top.",
        "For each new day, while the top of the stack is colder, pop it and set its answer to `today - popped_index`. Then push today. Each day is pushed and popped once, so it is O(n).",
    ],
    26: [
        "A car's own arrival time is easy to compute if nothing blocks it. How?",
        "Sort cars by starting position, closest to the target first, and compute each car's time `(target - position) / speed`.",
        "Go through the sorted cars. If a car's time is greater than the time of the fleet ahead of it, it starts a new fleet; otherwise it catches up and joins that fleet. Count the new fleets.",
    ],
    27: [
        "For any bar, the best rectangle that uses its full height extends left and right until it meets a shorter bar.",
        "So for each bar you need the nearest shorter bar on each side. A stack of increasing heights finds those in one pass.",
        "Keep a stack of `(start_index, height)`. When a new bar is shorter, pop the taller bars, compute `height * (i - start)` for each, and give the new bar the earliest `start` among the popped ones. Append a `0` bar at the end to flush the stack.",
    ],
}

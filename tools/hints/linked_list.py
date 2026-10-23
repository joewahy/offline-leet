HINTS = {
    38: [
        "The new order alternates between the front of the list and the back. You cannot walk backwards in a singly linked list, so what can you prepare?",
        "Split the list at its middle, reverse the second half, then weave the two halves together one node at a time.",
        "Find the middle with slow and fast pointers, cut the list there (`slow.next = None`), reverse the second part, then repeatedly link `first -> second -> first's old next -> ...`. This needs O(1) extra space.",
    ],
    39: [
        "Counting from the end seems to need the length. Can you avoid a first pass over the whole list?",
        "Use two pointers: move the lead pointer `n` steps ahead, then move both until the lead reaches the end.",
        "Start both at a dummy node placed before the head. When the lead is at the last node, the trailing pointer is just before the node to remove, so set `trail.next = trail.next.next`. The dummy handles removing the head.",
    ],
    40: [
        "The hard part is the `random` pointer: it may point to a node you have not copied yet.",
        "Make all the copies first, remembering which original maps to which copy. Then wire up `next` and `random` using that mapping.",
        "Use a dictionary `copies[original] = new node` (with `None` mapping to `None`). The first pass creates the nodes; the second pass sets `copy.next = copies[orig.next]` and `copy.random = copies[orig.random]`.",
    ],
    41: [
        "The digits are stored with the least significant digit first, which is the order you add in on paper.",
        "Walk both lists together, adding the two digits plus a carry, and build the result list as you go.",
        "At each step `total = a + b + carry`; append `total % 10` and carry `total // 10`. Keep going while either list has nodes or the carry is nonzero. A dummy head node simplifies building the result.",
    ],
    42: [
        "The values are between 1 and `n` and the array has `n + 1` entries. Treat each value as a pointer to another index.",
        "Following `i -> nums[i]` must eventually repeat, so it forms a cycle, and the duplicate value is where the cycle begins.",
        "Use Floyd's algorithm: find where a slow and a fast pointer meet, then restart one pointer from index 0 and move both one step at a time. They meet at the cycle entrance, which is the duplicate.",
    ],
    43: [
        "You need O(1) lookup by key and O(1) updates to the usage order. One structure alone cannot do both.",
        "Combine a hash map (key to node) with a doubly linked list ordered from least to most recently used.",
        "On `get` or `put`, move the node to the most-recent end. When the size exceeds the capacity, remove the node at the least-recent end and delete its key from the map. Dummy head and tail nodes avoid edge cases. (In Python, `OrderedDict` with `move_to_end` does the same job.)",
    ],
    44: [
        "Merging two sorted lists is easy. How could you reuse that idea for `k` lists?",
        "Either merge pairs of lists repeatedly (like merge sort), or keep a min-heap holding the current head of each list.",
        "With a heap, pop the smallest node, append it to the result, and push that node's `next`. Store `(value, list_index, node)` so ties never compare nodes. This is O(N log k) for N total nodes.",
    ],
    45: [
        "Handle one group at a time. First check whether `k` nodes are left.",
        "For a full group, reverse just those `k` nodes, then reconnect the group to the part before it and the part after it.",
        "Keep `group_prev` (the node before the group). Find the `k`-th node; if it does not exist, stop. Reverse the nodes up to `kth.next`, then set `group_prev.next = kth` and move `group_prev` to the old first node of the group. A dummy head helps.",
    ],
}

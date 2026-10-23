HINTS = {
    77: [
        "Each letter of a word can be a step down a tree. What does a node need to store?",
        "Each node holds a dictionary from letter to child node, plus a flag saying whether a word ends there.",
        "`insert` walks down, creating missing children, and sets the end flag. `search` walks down and checks the flag. `startsWith` walks down and only checks that the path exists.",
    ],
    78: [
        "Without wildcards this is the normal trie. What changes when `.` appears?",
        "Use a trie. When the next character is a letter, follow that child; when it is `.`, you must try every child.",
        "Write `search` as a recursive function `go(node, i)`. For `.`, return true if any child's `go(child, i + 1)` is true. At the end of the word, return whether the node is marked as the end of a word.",
    ],
    79: [
        "Running Word Search once per word repeats a lot of work. How could you search for all the words at once?",
        "Insert all the words into a trie, then explore the board with DFS, following trie children as you move.",
        "Stop exploring a path as soon as the current prefix is not in the trie. Store the full word at its end node so you can collect it, and remove found words (or prune empty branches) to avoid duplicates and speed up later searches.",
    ],
}

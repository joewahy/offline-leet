from spec import P
from specs.backtracking import _board, _words2

CATEGORY = "tries"


def _trie_ops(rng, m, alphabet="abc", name="PrefixTree"):
    ops, params = [name], [[]]
    for _ in range(m):
        word = "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 5)))
        ops.append(rng.choice(["insert", "search", "startsWith"]))
        params.append([word])
    return [ops, params]


def _wd_ops(rng, m):
    ops, params = ["WordDictionary"], [[]]
    for _ in range(m):
        if rng.random() < 0.4:
            ops.append("addWord")
            params.append(["".join(rng.choice("abc") for _ in range(rng.randint(1, 4)))])
        else:
            ops.append("search")
            params.append(["".join(rng.choice("abc..") for _ in range(rng.randint(1, 4)))])
    return [ops, params]


def _find_words_gen(rng):
    out = []
    for r, c in ((2, 2), (3, 3), (3, 4), (4, 4)):
        board = _board(rng, r, c, "abc")
        words = sorted({"".join(rng.choice("abc") for _ in range(rng.randint(2, 5))) for _ in range(rng.randint(3, 12))})
        out.append([board, words])
    out.append(_words2(rng))
    return out


def _find_words_small(rng):
    board = _board(rng, rng.randint(1, 3), rng.randint(1, 3), "ab")
    words = sorted({"".join(rng.choice("ab") for _ in range(rng.randint(1, 4))) for _ in range(rng.randint(1, 6))})
    return [board, words]


PROBLEMS = [
    P(77, "Implement Trie (Prefix Tree)", "Medium", "PrefixTree",
      r'''
A trie (prefix tree) stores strings so that you can quickly check whether a word, or a prefix of some word, has been stored.

Implement the class `PrefixTree`:

- `PrefixTree()` creates an empty trie.
- `insert(word)` stores `word`.
- `search(word)` returns `True` if exactly `word` was inserted, otherwise `False`.
- `startsWith(prefix)` returns `True` if some inserted word starts with `prefix`, otherwise `False`.

## Examples

```
insert("Hello")
search("Hello")      -> True
search("Hell")       -> False
startsWith("Hell")   -> True
insert("Hell")
search("Hell")       -> True
```

## Constraints

- `1 <= len(word), len(prefix) <= 1000`
- Strings consist of English letters.
- At most `10000` calls are made.

## Hints

- Each node holds a dictionary of children and a flag that says whether a word ends there.
''',
      r'''
class PrefixTree:

    def __init__(self):
        pass

    def insert(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
        pass

    def startsWith(self, prefix: str) -> bool:
        pass
''',
      r'''
class PrefixTree:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node["$"] = True

    def _find(self, s):
        node = self.root
        for c in s:
            if c not in node:
                return None
            node = node[c]
        return node

    def search(self, word):
        node = self._find(word)
        return node is not None and "$" in node

    def startsWith(self, prefix):
        return self._find(prefix) is not None
''',
      [([["PrefixTree", "insert", "search", "search", "startsWith", "insert", "search"],
         [[], ["Hello"], ["Hello"], ["Hell"], ["Hell"], ["Hell"], ["Hell"]]], [None, None, True, False, True, None, True]),
       ([["PrefixTree", "insert", "search", "search", "startsWith", "insert", "search"],
         [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]], [None, None, True, False, True, None, True]),
       ([["PrefixTree", "search", "startsWith", "insert", "startsWith", "startsWith"],
         [[], ["a"], ["a"], ["abc"], ["abd"], ["ab"]]], [None, False, False, None, False, True])],
      design="PrefixTree",
      gen=lambda rng: [_trie_ops(rng, m) for m in (15, 50, 200, 3000)],
      small=lambda rng: _trie_ops(rng, rng.randint(1, 14), "ab"),
      brute=r'''
class PrefixTree:
    def __init__(self):
        self.words = set()

    def insert(self, word):
        self.words.add(word)

    def search(self, word):
        return word in self.words

    def startsWith(self, prefix):
        return any(w.startswith(prefix) for w in self.words)
'''),

    P(78, "Design Add and Search Words Data Structure", "Medium", "WordDictionary",
      r'''
Design a data structure that stores words and can search them with a wildcard.

Implement the class `WordDictionary`:

- `WordDictionary()` creates an empty dictionary.
- `addWord(word)` stores `word`.
- `search(word)` returns `True` if some stored word matches `word`, otherwise `False`. In `word`, the character `.` matches any single letter. All other characters must match exactly, and the lengths must be equal.

## Examples

```
addWord("bad"); addWord("dad"); addWord("mad")
search("pad")   -> False
search("bad")   -> True
search(".ad")   -> True
search("b..")   -> True
```

## Constraints

- `1 <= len(word) <= 20`
- `addWord` words contain lowercase letters; `search` words contain lowercase letters and `.`
- At most `10000` calls are made, and at most 2 dots appear in any searched word.

## Hints

- Use a trie. When you meet a `.`, try every child at that level.
''',
      r'''
class WordDictionary:

    def __init__(self):
        pass

    def addWord(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
        pass
''',
      r'''
class WordDictionary:
    def __init__(self):
        self.root = {}

    def addWord(self, word):
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node["$"] = True

    def search(self, word):
        def go(node, i):
            if i == len(word):
                return "$" in node
            c = word[i]
            if c == ".":
                return any(go(child, i + 1) for key, child in node.items() if key != "$")
            return c in node and go(node[c], i + 1)

        return go(self.root, 0)
''',
      [([["WordDictionary", "addWord", "addWord", "addWord", "search", "search", "search", "search"],
         [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]]],
        [None, None, None, None, False, True, True, True]),
       ([["WordDictionary", "addWord", "search", "search", "search"], [[], ["a"], ["."], ["a."], ["..a"]]],
        [None, None, True, False, False]),
       ([["WordDictionary", "search", "addWord", "search", "search"], [[], ["."], ["abc"], ["a.c"], ["ab"]]],
        [None, False, None, True, False])],
      design="WordDictionary",
      gen=lambda rng: [_wd_ops(rng, m) for m in (15, 50, 200, 3000)],
      small=lambda rng: _wd_ops(rng, rng.randint(1, 14)),
      brute=r'''
class WordDictionary:
    def __init__(self):
        self.words = []

    def addWord(self, word):
        self.words.append(word)

    def search(self, word):
        return any(len(w) == len(word) and all(a == b or b == "." for a, b in zip(w, word)) for w in self.words)
'''),

    P(79, "Word Search II", "Hard", "findWords",
      r'''
Given a grid of characters `board` and a list of distinct strings `words`, return every word from the list that can be spelled by walking through horizontally or vertically adjacent cells. Each cell may be used at most once within a single word. The answer may be in any order.

## Examples

```
Input:  board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
        words = ["oath", "pea", "eat", "rain"]
Output: ["eat", "oath"]

Input:  board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
```

## Constraints

- `1 <= rows, cols <= 12`
- `1 <= len(words) <= 3000`
- `1 <= len(words[i]) <= 10`
- `board` and `words[i]` consist of lowercase letters; all words are distinct.

## Hints

- Searching each word separately repeats a lot of work. Put all the words in a trie and search the board once.
- Prune trie branches that cannot lead to a word any more.
''',
      r'''
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        pass
''',
      r'''
class Solution:
    def findWords(self, board, words):
        root = {}
        for w in words:
            node = root
            for c in w:
                node = node.setdefault(c, {})
            node["$"] = w
        rows, cols = len(board), len(board[0])
        found = []

        def dfs(r, c, parent):
            ch = board[r][c]
            node = parent.get(ch)
            if node is None:
                return
            if "$" in node:
                found.append(node.pop("$"))
            board[r][c] = "#"
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, node)
            board[r][c] = ch
            if not node:
                del parent[ch]

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
        return found
''',
      [([[["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
         ["oath", "pea", "eat", "rain"]], ["eat", "oath"]),
       ([[["a", "b"], ["c", "d"]], ["abcb"]], []), ([[["a"]], ["a"]], ["a"]),
       ([[["a", "b"], ["c", "d"]], ["ab", "cb", "ad", "bd", "ac", "ca", "da", "bc", "db", "adcb", "dabc", "abb", "acb"]],
        ["ab", "ac", "bd", "ca", "db"])],
      compare="unordered",
      gen=_find_words_gen, small=_find_words_small,
      brute=r'''
class Solution:
    def findWords(self, board, words):
        rows, cols = len(board), len(board[0])

        def go(r, c, w, used):
            if board[r][c] != w[0]:
                return False
            if len(w) == 1:
                return True
            used = used | {(r, c)}
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in used and go(nr, nc, w[1:], used):
                    return True
            return False

        return [w for w in words if any(go(r, c, w, frozenset()) for r in range(rows) for c in range(cols))]
'''),
]

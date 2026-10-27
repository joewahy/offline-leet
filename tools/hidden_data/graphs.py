GRID_SIZE = ("`1 <= rows, cols <= 60`", "`1 <= rows, cols`, and `rows * cols <= 10^5`")

LAYERED_DAG = \
    '''
    layers, width = 50, 1000
    n = layers * width
    label = list(range(n))
    rng.shuffle(label)
    requires = {}
    for layer in range(1, layers):
        for i in range(width):
            node = layer * width + i
            requires[node] = [(layer - 1) * width + j for j in rng.sample(range(width), 2)]
    edges = [[label[a], label[b]] for a, bs in requires.items() for b in bs]
    rng.shuffle(edges)
    top = layers * width - 1 - rng.randrange(width)
    low = top
    while low >= width:
        low = rng.choice(requires[low])
    cyclic = edges + [[label[low], label[top]]]
    rng.shuffle(cyclic)
'''

HIDDEN = {
    83: ([GRID_SIZE], '''
def generate(rng):
    inf = 2147483647
    n = 316
    scattered = [[rng.choices([-1, 0, inf], [20, 1, 79])[0] for _ in range(n)] for _ in range(n)]
    diagonal = [[0 if r == c else inf for c in range(n)] for r in range(n)]
    corner = [[inf] * n for _ in range(n)]
    corner[0][0] = 0
    return [[scattered], [diagonal], [corner]]
'''),
    84: ([GRID_SIZE], '''
def generate(rng):
    n = 315
    snake = []
    for r in range(n):
        if r % 2 == 0:
            snake.append([1] * n)
        else:
            row = [0] * n
            row[n - 1 if (r // 2) % 2 == 0 else 0] = 1
            snake.append(row)
    snake[0][0] = 2
    scattered = [[rng.choices([0, 1, 2], [10, 80, 10])[0] for _ in range(316)] for _ in range(316)]
    one_source = [[1] * 316 for _ in range(316)]
    one_source[158][158] = 2
    return [[snake], [scattered], [one_source]]
'''),
    85: ([
        ("`1 <= rows, cols <= 30`", "`1 <= rows, cols`, and `rows * cols <= 10^5`"),
        ("`0 <= heights[r][c] <= 100`", "`0 <= heights[r][c] <= 10^5`"),
    ], '''
def generate(rng):
    n = 316
    centre = n // 2
    slope = [[r * n + c for c in range(n)] for r in range(n)]
    hill = [[50000 - ((r - centre) ** 2 + (c - centre) ** 2) for c in range(n)] for r in range(n)]
    scattered = [[rng.randint(0, 100) for _ in range(n)] for _ in range(n)]
    return [[slope], [hill], [scattered]]
'''),
    87: ([
        ("`1 <= numCourses <= 2000`", "`1 <= numCourses <= 10^5`"),
        ("`0 <= len(prerequisites) <= 3000`", "`0 <= len(prerequisites) <= 10^5`"),
    ], '''
def generate(rng):''' + LAYERED_DAG + '''    return [[n, edges], [n, cyclic]]
'''),
    88: ([
        ("`1 <= numCourses <= 2000`", "`1 <= numCourses <= 10^5`"),
        ("`0 <= len(prerequisites) <= 3000`", "`0 <= len(prerequisites) <= 10^5`"),
    ], '''
def generate(rng):''' + LAYERED_DAG + '''    return [[n, edges], [n, cyclic]]
'''),
    90: ([
        ("`1 <= n <= 5000`", "`1 <= n <= 10^5`"),
        ("`0 <= len(edges) <= 5000`", "`0 <= len(edges) <= 10^5`"),
    ], '''
def generate(rng):
    n = 100000
    label = list(range(n))
    rng.shuffle(label)

    def finish(pairs):
        edges = [[label[a], label[b]] if rng.random() < 0.5 else [label[b], label[a]] for a, b in pairs]
        rng.shuffle(edges)
        return [n, edges]

    tree = [(rng.randrange(i), i) for i in range(1, n)]
    pairs = set()
    while len(pairs) < 40000:
        a, b = rng.sample(range(n), 2)
        pairs.add((min(a, b), max(a, b)))
    forest = [(rng.randrange(i - i % 10, i), i) for i in range(1, n) if i % 10]
    return [finish(tree), finish(sorted(pairs)), finish(forest)]
'''),
    91: ([("`3 <= n <= 1000`, and `len(edges) == n`", "`3 <= n <= 10^5`, and `len(edges) == n`")], '''
def generate(rng):
    n = 100000
    cases = []
    for extra_last in (False, True):
        label = list(range(1, n + 1))
        rng.shuffle(label)
        tree = [(rng.randrange(i), i) for i in range(1, n)]
        seen = set(tree)
        while True:
            a, b = rng.sample(range(n), 2)
            if (min(a, b), max(a, b)) not in seen:
                break
        edges = [[label[a], label[b]] if rng.random() < 0.5 else [label[b], label[a]] for a, b in tree]
        rng.shuffle(edges)
        extra = [label[a], label[b]]
        if extra_last:
            edges.append(extra)
        else:
            edges.insert(rng.randrange(len(edges) + 1), extra)
        cases.append([edges])
    return cases
'''),
    92: ([("`1 <= len(wordList) <= 3000`, and every word has the same length",
           "`1 <= len(wordList) <= 5 * 10^4`, and every word has the same length")], '''
def generate(rng):
    def words_over(alphabet, length, count):
        words = set()
        while len(words) < count:
            words.add("".join(rng.choice(alphabet) for _ in range(length)))
        return sorted(words)

    def ladder(alphabet, length, count, reachable):
        words = words_over(alphabet, length, count)
        rng.shuffle(words)
        begin = words.pop()
        end = words[0] if reachable else "".join(rng.choice(alphabet) for _ in range(length))
        return [begin, end, words]

    return [
        ladder("abcde", 8, 40000, True),
        ladder("abc", 10, 30000, True),
        ladder("abcde", 8, 40000, False),
    ]
'''),
}

HIDDEN = {
    95: ([
        ("`1 <= k <= n <= 1000`", "`1 <= k <= n <= 10^5`"),
        ("`0 <= len(times) <= 5000`", "`0 <= len(times) <= 10^5`"),
    ], '''
def generate(rng):
    def random_edges(n, count, lowest, highest, taken):
        times = []
        while len(times) < count:
            u, v = rng.sample(range(1, n + 1), 2)
            if (u, v) not in taken:
                taken.add((u, v))
                times.append([u, v, rng.randint(lowest, highest)])
        return times

    n = 50000
    order = list(range(1, n + 1))
    rng.shuffle(order)
    taken = {(order[i], order[i + 1]) for i in range(n - 1)}
    chain = [[order[i], order[i + 1], rng.randint(1, 10)] for i in reversed(range(n - 1))]
    extra = []
    while len(extra) < 50000:
        if len(extra) % 2:
            i = rng.randrange(n - 8)
            j = i + rng.randint(2, 8)
            weight = 10 * (j - i) + rng.randint(1, 10)
        else:
            i = rng.randrange(1, n)
            j = rng.randrange(i)
            weight = rng.randint(1, 100)
        if (order[i], order[j]) not in taken:
            taken.add((order[i], order[j]))
            extra.append([order[i], order[j], weight])
    half = len(chain) // 2
    mixed = chain[:half] + extra + chain[half:]

    sparse = random_edges(20000, 15000, 1, 100, set())
    route = list(range(1, 30001))
    rng.shuffle(route)
    taken = {(route[i], route[i + 1]) for i in range(29999)}
    dense = [[route[i], route[i + 1], rng.randint(1, 100)] for i in range(29999)]
    dense += random_edges(30000, 70001, 1, 100, taken)
    rng.shuffle(dense)
    return [[mixed, n, order[0]], [sparse, 20000, 1], [dense, 30000, route[0]]]
'''),
    96: ([("`1 <= n <= 40`", "`1 <= n`, and `n * n <= 10^5`")], '''
def generate(rng):
    n = 299
    values = list(range(n * n))
    rng.shuffle(values)
    scattered = [values[r * n:(r + 1) * n] for r in range(n)]
    snake = [[r * n + (c if r % 2 == 0 else n - 1 - c) for c in range(n)] for r in range(n)]
    columns = [[c * n + (r if c % 2 == 0 else n - 1 - r) for c in range(n)] for r in range(n)]
    return [[scattered], [snake], [columns]]
'''),
}

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

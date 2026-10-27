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

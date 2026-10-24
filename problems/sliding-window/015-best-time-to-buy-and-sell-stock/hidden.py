def generate(rng):
    n = 100000
    walk = [500]
    for _ in range(n - 1):
        walk.append(min(1000, max(0, walk[-1] + rng.randint(-3, 3))))
    return [[walk], [list(range(1000, 1000 - n, -1))], [[rng.randint(0, 1000) for _ in range(n)]]]

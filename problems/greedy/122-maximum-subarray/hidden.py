def generate(rng):
    n = 100000
    return [
        [[rng.randint(-1000, 1000) for _ in range(n)]],
        [[-rng.randint(1, 1000) for _ in range(n)]],
        [[rng.randint(-900, 1000) for _ in range(n)]],
    ]

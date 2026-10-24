def generate(rng):
    n = 100000
    return [
        [[1] * n],
        [[rng.randint(1, 100) for _ in range(n)]],
        [[rng.randint(1, 3) for _ in range(n)]],
    ]

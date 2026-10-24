def generate(rng):
    n = 100000
    return [
        [[rng.randint(1, 10**9) for _ in range(n)]],
        [[rng.randint(10**8, 10**9) for _ in range(n)]],
        [[rng.randint(1, 1000) for _ in range(n)]],
        [[1000] * n],
    ]

def generate(rng):
    n = 100000
    return [
        [[rng.randint(0, 10000) for _ in range(n)]],
        [[10000] * n],
        [[i * 10000 // n for i in range(n)]],
    ]

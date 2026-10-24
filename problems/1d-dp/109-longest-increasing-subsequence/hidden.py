def generate(rng):
    n = 100000
    return [
        [[rng.randint(-10000, 10000) for _ in range(n)]],
        [[i * 20000 // n - 10000 for i in range(n)]],
        [[10000 - i * 20000 // n for i in range(n)]],
        [[(i % 1000) * 20 - 10000 + rng.randint(0, 5) for i in range(n)]],
    ]

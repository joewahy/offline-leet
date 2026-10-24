def generate(rng):
    n = 100000
    return [
        [[rng.randint(0, 10000) for _ in range(n)]],
        [[i % 10001 for i in range(n)]],
        [[10000 - i * 10000 // n for i in range(n)]],
    ]

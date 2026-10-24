def generate(rng):
    n = 100000
    return [
        [[70] * n],
        [[rng.randint(30, 100) for _ in range(n)]],
        [[100 - i * 70 // (n // 2) for i in range(n // 2)] + [30 + i * 70 // (n // 2) for i in range(n // 2)]],
    ]

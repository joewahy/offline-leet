def generate(rng):
    n = 100000
    walled = [1000] * n
    walled[n // 2 - 500:n // 2 + 500] = [0] * 1000
    return [
        [[1000] * (n - 1) + [0]],
        [walled],
        [[rng.randint(1, 3) for _ in range(n - 1)] + [0]],
        [[rng.choice((0, 0, 1, 2)) for _ in range(n)]],
    ]

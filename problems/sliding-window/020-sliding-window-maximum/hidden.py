def generate(rng):
    n = 100000
    values = [rng.randint(-10000, 10000) for _ in range(n)]
    return [[values, n // 2], [sorted(values), n // 4], [values, 1], [values, n]]

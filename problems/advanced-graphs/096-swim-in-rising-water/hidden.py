def generate(rng):
    n = 299
    values = list(range(n * n))
    rng.shuffle(values)
    scattered = [values[r * n:(r + 1) * n] for r in range(n)]
    snake = [[r * n + (c if r % 2 == 0 else n - 1 - c) for c in range(n)] for r in range(n)]
    columns = [[c * n + (r if c % 2 == 0 else n - 1 - r) for c in range(n)] for r in range(n)]
    return [[scattered], [snake], [columns]]

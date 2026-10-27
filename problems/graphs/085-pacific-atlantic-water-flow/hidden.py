def generate(rng):
    n = 316
    centre = n // 2
    slope = [[r * n + c for c in range(n)] for r in range(n)]
    hill = [[50000 - ((r - centre) ** 2 + (c - centre) ** 2) for c in range(n)] for r in range(n)]
    scattered = [[rng.randint(0, 100) for _ in range(n)] for _ in range(n)]
    return [[slope], [hill], [scattered]]

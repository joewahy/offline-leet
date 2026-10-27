def generate(rng):
    inf = 2147483647
    n = 316
    scattered = [[rng.choices([-1, 0, inf], [20, 1, 79])[0] for _ in range(n)] for _ in range(n)]
    diagonal = [[0 if r == c else inf for c in range(n)] for r in range(n)]
    corner = [[inf] * n for _ in range(n)]
    corner[0][0] = 0
    return [[scattered], [diagonal], [corner]]

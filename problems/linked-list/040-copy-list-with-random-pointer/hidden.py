def generate(rng):
    n = 100000
    cases = []
    for null_rate in (0.2, 0.0):
        nodes = [[rng.randint(-100, 100), None if rng.random() < null_rate else rng.randrange(n)] for _ in range(n)]
        cases.append([nodes])
    return cases

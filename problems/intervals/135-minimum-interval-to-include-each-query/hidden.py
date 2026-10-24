def generate(rng):
    n = 100000
    cases = []
    for max_length in (100, 100000, 1000000):
        intervals = []
        for _ in range(n):
            left = rng.randint(1, 10**6)
            intervals.append([left, min(10**6, left + rng.randint(0, max_length))])
        cases.append([intervals, [rng.randint(1, 10**6) for _ in range(n)]])
    return cases

def generate(rng):
    n = 100000
    cases = []
    for k, heavy_low, heavy_high in ((10, 4000, 4500), (1000, 60, 80)):
        values = rng.sample(range(-10**9, 10**9 + 1), 50000)
        counts = {v: rng.randint(heavy_low, heavy_high) for v in values[:k]}
        rest = values[k:]
        for v in rest:
            counts[v] = 0
        for _ in range(n - sum(counts.values())):
            counts[rng.choice(rest)] += 1
        nums = [v for v, c in counts.items() for _ in range(c)]
        rng.shuffle(nums)
        cases.append([nums, k])
    return cases

def generate(rng):
    n = 100000
    cases = []
    for missing in (rng.randint(0, n), 0, n):
        nums = [v for v in range(n + 1) if v != missing]
        rng.shuffle(nums)
        cases.append([nums])
    return cases

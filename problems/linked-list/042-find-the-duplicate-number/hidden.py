def generate(rng):
    n = 100000
    cases = []
    for copies in (2, 3, 50000):
        d = rng.randint(1, n)
        others = rng.sample([v for v in range(1, n + 1) if v != d], n + 1 - copies)
        nums = [d] * copies + others
        rng.shuffle(nums)
        cases.append([nums])
    return cases

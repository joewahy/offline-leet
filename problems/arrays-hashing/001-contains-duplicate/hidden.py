def generate(rng):
    n = 100000
    distinct = rng.sample(range(-10**9, 10**9), n)
    return [[distinct], [distinct[:-1] + [distinct[n // 2]]]]

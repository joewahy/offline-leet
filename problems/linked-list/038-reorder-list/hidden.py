def generate(rng):
    return [[[rng.randint(1, 1000) for _ in range(n)]] for n in (100000, 99999)]

def generate(rng):
    chain = [str(rng.randint(-1000, 1000))]
    for _ in range(49999):
        chain += [str(rng.randint(-1000, 1000)), rng.choice(["+", "-"])]
    wide = [str(rng.randint(-1000, 1000)) for _ in range(50000)] + ["+"] * 49999
    return [[chain], [wide]]

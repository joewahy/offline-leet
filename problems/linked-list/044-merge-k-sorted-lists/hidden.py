def generate(rng):
    def lists(k, longest):
        return [sorted(rng.randint(-1000, 1000) for _ in range(rng.randint(0, longest))) for _ in range(k)]

    uneven = lists(4999, 10)
    uneven.insert(rng.randrange(len(uneven)), sorted(rng.randint(-1000, 1000) for _ in range(50000)))
    return [[lists(5000, 40)], [lists(100, 2000)], [uneven]]

def generate(rng):
    n = 100000

    def intervals(max_length):
        out = []
        for _ in range(n):
            start = rng.randint(0, 10**6 - max_length)
            out.append([start, start + rng.randint(1, max_length)])
        return out

    stacked = [[i, 10**6 - i] for i in range(n)]
    rng.shuffle(stacked)
    return [[intervals(50)], [intervals(100000)], [stacked]]

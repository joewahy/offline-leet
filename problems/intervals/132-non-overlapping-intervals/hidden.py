def generate(rng):
    n = 100000

    def intervals(max_length):
        out = []
        for _ in range(n):
            start = rng.randint(0, 10**6 - max_length)
            out.append([start, start + rng.randint(1, max_length)])
        return out

    disjoint = [[10 * i, 10 * i + rng.randint(1, 10)] for i in range(n)]
    rng.shuffle(disjoint)
    return [[intervals(5)], [intervals(1000)], [disjoint]]

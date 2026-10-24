def generate(rng):
    n = 100000
    disjoint = [[10 * i, 10 * i + rng.randint(1, 10)] for i in range(n)]
    rng.shuffle(disjoint)
    touching = [[i, i + 1] for i in range(n)]
    rng.shuffle(touching)
    one_clash = [row[:] for row in sorted(disjoint)]
    k = rng.randrange(1, n)
    one_clash[k - 1][1] = 10 * k + 1
    rng.shuffle(one_clash)
    return [[disjoint], [touching], [one_clash]]

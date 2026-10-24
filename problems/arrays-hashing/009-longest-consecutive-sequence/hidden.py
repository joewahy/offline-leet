def generate(rng):
    n = 100000
    one_run = list(range(n))
    rng.shuffle(one_run)
    no_runs = [2 * v - 10**9 for v in range(n)]
    rng.shuffle(no_runs)
    pieces = []
    start = -10**9
    for length in (40000, 30000, 20000, 10000):
        pieces.extend(range(start, start + length))
        start += length + 5
    rng.shuffle(pieces)
    return [[one_run], [no_runs], [pieces]]

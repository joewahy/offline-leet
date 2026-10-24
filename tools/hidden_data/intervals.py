HIDDEN = {
    131: ([("`1 <= len(intervals) <= 10000`", "`1 <= len(intervals) <= 10^5`")], '''
def generate(rng):
    n = 100000

    def intervals(max_length):
        out = []
        for _ in range(n):
            start = rng.randint(0, 10**6 - max_length)
            out.append([start, start + rng.randint(0, max_length)])
        return out

    disjoint = [[10 * i, 10 * i + rng.randint(0, 9)] for i in range(n)]
    rng.shuffle(disjoint)
    return [[intervals(5)], [intervals(1000)], [disjoint]]
'''),
    132: ([("`1 <= len(intervals) <= 10000`", "`1 <= len(intervals) <= 10^5`")], '''
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
'''),
    133: ([("`0 <= len(intervals) <= 8000`", "`0 <= len(intervals) <= 10^5`")], '''
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
'''),
    134: ([("`0 <= len(intervals) <= 8000`", "`0 <= len(intervals) <= 10^5`")], '''
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
'''),
    135: ([("`1 <= len(intervals), len(queries) <= 7000`", "`1 <= len(intervals), len(queries) <= 10^5`")], '''
def generate(rng):
    n = 100000
    cases = []
    for max_length in (100, 100000, 1000000):
        intervals = []
        for _ in range(n):
            left = rng.randint(1, 10**6)
            intervals.append([left, min(10**6, left + rng.randint(0, max_length))])
        cases.append([intervals, [rng.randint(1, 10**6) for _ in range(n)]])
    return cases
'''),
}

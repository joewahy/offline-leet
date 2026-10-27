HIDDEN = {
    38: ([("`1 <= number of nodes <= 5000`", "`1 <= number of nodes <= 10^5`")], '''
def generate(rng):
    return [[[rng.randint(1, 1000) for _ in range(n)]] for n in (100000, 99999)]
'''),
    40: ([("`0 <= number of nodes <= 1000`", "`0 <= number of nodes <= 10^5`")], '''
def generate(rng):
    n = 100000
    cases = []
    for null_rate in (0.2, 0.0):
        nodes = [[rng.randint(-100, 100), None if rng.random() < null_rate else rng.randrange(n)] for _ in range(n)]
        cases.append([nodes])
    return cases
'''),
    42: ([("`1 <= n <= 10000`", "`1 <= n <= 10^5`")], '''
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
'''),
    43: ([
        ("`1 <= capacity <= 100`", "`1 <= capacity <= 10^5`"),
        ("`0 <= key <= 1000`", "`0 <= key <= 10^5`"),
        ("At most `10000` calls are made.", "At most `10^5` calls are made."),
    ], '''
def generate(rng):
    def run(capacity, keys, hot=0):
        ops, params = ["LRUCache"], [[capacity]]
        filled = list(range(capacity)) if not hot else []
        rng.shuffle(filled)
        for key in filled:
            ops.append("put")
            params.append([key, rng.randint(0, 10**5)])
        for _ in range(99999 - len(filled)):
            key = rng.randrange(hot if hot and rng.random() < 0.8 else keys)
            if rng.random() < 0.5:
                ops.append("put")
                params.append([key, rng.randint(0, 10**5)])
            else:
                ops.append("get")
                params.append([key])
        return [ops, params]

    return [run(50000, 60000), run(5000, 20000, hot=3000)]
'''),
    44: ([
        ("`0 <= k <= 100`", "`0 <= k <= 10^4`"),
        ("`0 <= length of each list <= 100`, and the total number of nodes is at most `10000`",
         "`0 <= length of each list <= 10^5`, and the total number of nodes is at most `10^5`"),
    ], '''
def generate(rng):
    def lists(k, longest):
        return [sorted(rng.randint(-1000, 1000) for _ in range(rng.randint(0, longest))) for _ in range(k)]

    uneven = lists(4999, 10)
    uneven.insert(rng.randrange(len(uneven)), sorted(rng.randint(-1000, 1000) for _ in range(50000)))
    return [[lists(5000, 40)], [lists(100, 2000)], [uneven]]
'''),
}

HIDDEN = {
    122: ([("`1 <= len(nums) <= 10000`", "`1 <= len(nums) <= 10^5`")], '''
def generate(rng):
    n = 100000
    return [
        [[rng.randint(-1000, 1000) for _ in range(n)]],
        [[-rng.randint(1, 1000) for _ in range(n)]],
        [[rng.randint(-900, 1000) for _ in range(n)]],
    ]
'''),
    123: ([("`1 <= len(nums) <= 10000`", "`1 <= len(nums) <= 10^5`")], '''
def generate(rng):
    n = 100000
    walled = [1000] * n
    walled[n // 2 - 500:n // 2 + 500] = [0] * 1000
    return [
        [[1000] * (n - 1) + [0]],
        [walled],
        [[rng.randint(1, 3) for _ in range(n - 1)] + [0]],
        [[rng.choice((0, 0, 1, 2)) for _ in range(n)]],
    ]
'''),
    124: ([("`1 <= len(nums) <= 10000`", "`1 <= len(nums) <= 10^5`")], '''
def generate(rng):
    n = 100000
    return [
        [[1] * n],
        [[rng.randint(1, 100) for _ in range(n)]],
        [[rng.randint(1, 3) for _ in range(n)]],
    ]
'''),
    125: ([("`1 <= n <= 10000`", "`1 <= n <= 10^5`")], '''
def generate(rng):
    n = 100000
    cases = []
    for _ in range(2):
        while True:
            cost = [rng.randint(0, 1000) for _ in range(n)]
            gas = cost[:]
            rng.shuffle(gas)
            total, low = 0, []
            prefix = []
            for g, c in zip(gas, cost):
                prefix.append(total)
                total += g - c
            if prefix.count(min(prefix)) == 1:
                break
        cases.append([gas, cost])
    short = [rng.randint(0, 1000) for _ in range(n)]
    cases.append([[max(0, c - 1) for c in short], short])
    return cases
'''),
    126: ([("`1 <= len(hand) <= 10000`", "`1 <= len(hand) <= 10^5`")], '''
def generate(rng):
    cases = []
    for size, groups in ((1000, 100), (7, 14000), (1, 100000)):
        starts = rng.sample(range(0, 10**9, size + 1), groups)
        hand = [s + k for s in starts for k in range(size)]
        rng.shuffle(hand)
        cases.append([hand, size])
        broken = hand[:]
        broken[rng.randrange(len(broken))] += 1
        if size > 1:
            cases.append([broken, size])
    return cases
'''),
    129: ([("`1 <= len(s) <= 100`", "`1 <= len(s) <= 10^5`")], '''
def generate(rng):
    n = 100000
    third = n // 3
    cases = [
        "(" * third + "*" * (n - 2 * third) + ")" * third,
        "*" * n,
        "*" * (n // 2) + "(" * (n // 2),
        "".join(rng.choices("()*", [30, 30, 40], k=n)),
    ]
    depth, chars = 0, []
    for i in range(n):
        left = n - i
        if depth == left:
            chars.append(")")
        elif depth == 0 or rng.random() < 0.5:
            chars.append("(")
        else:
            chars.append(")")
        depth += 1 if chars[-1] == "(" else -1
    cases.append("".join(c if rng.random() > 0.3 else "*" for c in chars))
    cases.append(cases[-1][:-1] + "(")
    cases.append("(" * (n // 2) + "*" * (n // 2))
    cases.append("*" * (n // 2) + ")" * (n // 2))
    return [[s] for s in cases]
'''),
}

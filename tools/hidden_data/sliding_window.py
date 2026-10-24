HIDDEN = {
    15: ([("`1 <= len(prices) <= 10000`", "`1 <= len(prices) <= 10^5`")], '''
def generate(rng):
    n = 100000
    walk = [500]
    for _ in range(n - 1):
        walk.append(min(1000, max(0, walk[-1] + rng.randint(-3, 3))))
    return [[walk], [list(range(1000, 1000 - n, -1))], [[rng.randint(0, 1000) for _ in range(n)]]]
'''),
    16: ([("`0 <= len(s) <= 10000`", "`0 <= len(s) <= 10^5`")], '''
def generate(rng):
    n = 100000
    printable = [chr(c) for c in range(32, 127)]
    return [
        ["".join(rng.choice(printable) for _ in range(n))],
        ["a" * n],
        ["".join(printable[i % len(printable)] for i in range(n))],
    ]
'''),
    17: ([("`1 <= len(s) <= 10000`", "`1 <= len(s) <= 10^5`")], '''
def generate(rng):
    n = 100000
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return [
        ["".join(rng.choice("AB") for _ in range(n)), 1000],
        ["".join(rng.choice(letters) for _ in range(n)), n // 4],
        ["A" * n, 0],
    ]
'''),
    18: ([("`1 <= len(s1), len(s2) <= 10000`", "`1 <= len(s1), len(s2) <= 10^5`")], '''
def generate(rng):
    letters = "abcdefghijklmnopqrstuvwxyz"
    s1 = "".join(rng.choice(letters) for _ in range(50000))
    shuffled = list(s1)
    rng.shuffle(shuffled)
    junk = "".join(rng.choice(letters) for _ in range(50000))
    other = "".join(rng.choice(letters) for _ in range(100000))
    return [[s1, junk + "".join(shuffled)], [s1, other], ["a" * 40000 + "b", "a" * 100000]]
'''),
    19: ([("`1 <= len(s), len(t) <= 10000`", "`1 <= len(s), len(t) <= 10^5`")], '''
def generate(rng):
    n = 100000
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s = "".join(rng.choice(letters) for _ in range(n))
    t = "".join(rng.choice(letters) for _ in range(3000))
    return [[s, t], [s, "".join(sorted(set(letters)))], ["a" * n, "a" * 50000]]
'''),
    20: ([("`1 <= k <= len(nums) <= 10000`", "`1 <= k <= len(nums) <= 10^5`")], '''
def generate(rng):
    n = 100000
    values = [rng.randint(-10000, 10000) for _ in range(n)]
    return [[values, n // 2], [sorted(values), n // 4], [values, 1], [values, n]]
'''),
}

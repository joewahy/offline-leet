HIDDEN = {
    21: ([("`1 <= len(s) <= 10000`", "`1 <= len(s) <= 10^5`")], '''
def generate(rng):
    pairs = {"(": ")", "[": "]", "{": "}"}
    opens = [rng.choice("([{") for _ in range(50000)]
    nested = "".join(opens) + "".join(pairs[c] for c in reversed(opens))
    broken = list(nested)
    broken[50000] = ")" if broken[50000] != ")" else "]"
    flat = "".join(rng.choice(["()", "[]", "{}"]) for _ in range(50000))
    return [[nested], ["".join(broken)], [flat]]
'''),
    23: ([("`1 <= len(tokens) <= 10000`", "`1 <= len(tokens) <= 10^5`")], '''
def generate(rng):
    chain = [str(rng.randint(-1000, 1000))]
    for _ in range(49999):
        chain += [str(rng.randint(-1000, 1000)), rng.choice(["+", "-"])]
    wide = [str(rng.randint(-1000, 1000)) for _ in range(50000)] + ["+"] * 49999
    return [[chain], [wide]]
'''),
    25: ([("`1 <= len(temperatures) <= 10000`", "`1 <= len(temperatures) <= 10^5`")], '''
def generate(rng):
    n = 100000
    return [
        [[70] * n],
        [[rng.randint(30, 100) for _ in range(n)]],
        [[100 - i * 70 // (n // 2) for i in range(n // 2)] + [30 + i * 70 // (n // 2) for i in range(n // 2)]],
    ]
'''),
    26: ([("`1 <= len(position) == len(speed) <= 10000`", "`1 <= len(position) == len(speed) <= 10^5`")], '''
def generate(rng):
    n = 100000
    target = 10**6
    cases = []
    for max_speed in (100, 3):
        position = rng.sample(range(target), n)
        speed = [rng.randint(1, max_speed) for _ in range(n)]
        cases.append([target, position, speed])
    return cases
'''),
    27: ([("`1 <= len(heights) <= 8000`", "`1 <= len(heights) <= 10^5`")], '''
def generate(rng):
    n = 100000
    return [
        [[rng.randint(0, 10000) for _ in range(n)]],
        [[10000] * n],
        [[i * 10000 // n for i in range(n)]],
    ]
'''),
    22: ([("At most `10000` calls are made.", "At most `10^5` calls are made.")], '''
def generate(rng):
    ops, params = ["MinStack"], [[]]
    size = 0
    for i in range(100000 - 1):
        if size < 60000 and i < 60000:
            ops.append("push")
            params.append([rng.randint(-2**31, 2**31 - 1)])
            size += 1
            continue
        op = rng.choice(["getMin", "getMin", "top", "pop", "push"])
        if op == "pop" and size <= 1:
            op = "push"
        ops.append(op)
        if op == "push":
            params.append([rng.randint(-2**31, 2**31 - 1)])
            size += 1
        else:
            params.append([])
            size -= op == "pop"
    return [[ops, params]]
'''),
}

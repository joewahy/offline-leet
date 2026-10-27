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

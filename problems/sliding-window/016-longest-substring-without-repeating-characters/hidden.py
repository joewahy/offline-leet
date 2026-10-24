def generate(rng):
    n = 100000
    printable = [chr(c) for c in range(32, 127)]
    return [
        ["".join(rng.choice(printable) for _ in range(n))],
        ["a" * n],
        ["".join(printable[i % len(printable)] for i in range(n))],
    ]

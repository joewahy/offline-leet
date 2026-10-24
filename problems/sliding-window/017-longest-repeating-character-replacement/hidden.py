def generate(rng):
    n = 100000
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return [
        ["".join(rng.choice("AB") for _ in range(n)), 1000],
        ["".join(rng.choice(letters) for _ in range(n)), n // 4],
        ["A" * n, 0],
    ]

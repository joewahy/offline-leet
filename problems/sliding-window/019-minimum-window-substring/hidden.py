def generate(rng):
    n = 100000
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s = "".join(rng.choice(letters) for _ in range(n))
    t = "".join(rng.choice(letters) for _ in range(3000))
    return [[s, t], [s, "".join(sorted(set(letters)))], ["a" * n, "a" * 50000]]

def generate(rng):
    letters = "abcdefghijklmnopqrstuvwxyz"
    s1 = "".join(rng.choice(letters) for _ in range(50000))
    shuffled = list(s1)
    rng.shuffle(shuffled)
    junk = "".join(rng.choice(letters) for _ in range(50000))
    other = "".join(rng.choice(letters) for _ in range(100000))
    return [[s1, junk + "".join(shuffled)], [s1, other], ["a" * 40000 + "b", "a" * 100000]]

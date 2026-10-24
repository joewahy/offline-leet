def generate(rng):
    n = 100000
    printable = [chr(c) for c in range(32, 127)]
    half = "".join(rng.choice(printable) for _ in range(n // 2))
    noisy = "".join(c if rng.random() < 0.9 else rng.choice(" ,.!?") for c in half)
    palindrome = half + half[::-1]
    broken = list(palindrome)
    broken[n // 2 - 1] = "~" if broken[n // 2 - 1] != "~" else "}"
    return [[palindrome], ["".join(broken)], ["a" * n], [noisy + "x" + noisy[::-1]]]

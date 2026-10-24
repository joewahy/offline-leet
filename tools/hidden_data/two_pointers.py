HIDDEN = {
    11: ([("`2 <= len(numbers) <= 10000`", "`2 <= len(numbers) <= 10^5`")], '''
def generate(rng):
    n = 100000
    cases = []
    for place in ("ends", "middle", "random"):
        numbers = sorted(rng.sample(range(-10**6, 10**6), n))
        if place == "ends":
            i, j = 0, n - 1
        elif place == "middle":
            i, j = n // 2 - 1, n // 2
        else:
            i, j = sorted(rng.sample(range(n), 2))
        cases.append([numbers, numbers[i] + numbers[j]])
    return cases
'''),
    13: ([("`2 <= len(heights) <= 12000`", "`2 <= len(heights) <= 10^5`")], '''
def generate(rng):
    n = 100000
    return [
        [[rng.randint(0, 10000) for _ in range(n)]],
        [[i % 10001 for i in range(n)]],
        [[10000 - i * 10000 // n for i in range(n)]],
    ]
'''),
    14: ([("`1 <= len(height) <= 10000`", "`1 <= len(height) <= 10^5`")], '''
def generate(rng):
    n = 100000
    half = n // 2
    valley = [1000 - i * 1000 // half for i in range(half)] + [i * 1000 // half for i in range(half)]
    sawtooth = [(i % 2) * rng.randint(1, 1000) for i in range(n)]
    return [[[rng.randint(0, 1000) for _ in range(n)]], [valley], [sawtooth]]
'''),
    10: ([("`1 <= len(s) <= 20000`", "`1 <= len(s) <= 10^5`")], '''
def generate(rng):
    n = 100000
    printable = [chr(c) for c in range(32, 127)]
    half = "".join(rng.choice(printable) for _ in range(n // 2))
    noisy = "".join(c if rng.random() < 0.9 else rng.choice(" ,.!?") for c in half)
    palindrome = half + half[::-1]
    broken = list(palindrome)
    broken[n // 2 - 1] = "~" if broken[n // 2 - 1] != "~" else "}"
    return [[palindrome], ["".join(broken)], ["a" * n], [noisy + "x" + noisy[::-1]]]
'''),
}

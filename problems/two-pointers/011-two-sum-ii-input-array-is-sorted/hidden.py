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

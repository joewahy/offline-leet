def generate(rng):
    n = 100000
    target = 10**6
    cases = []
    for max_speed in (100, 3):
        position = rng.sample(range(target), n)
        speed = [rng.randint(1, max_speed) for _ in range(n)]
        cases.append([target, position, speed])
    return cases

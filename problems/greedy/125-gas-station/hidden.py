def generate(rng):
    n = 100000
    cases = []
    for _ in range(2):
        while True:
            cost = [rng.randint(0, 1000) for _ in range(n)]
            gas = cost[:]
            rng.shuffle(gas)
            total, low = 0, []
            prefix = []
            for g, c in zip(gas, cost):
                prefix.append(total)
                total += g - c
            if prefix.count(min(prefix)) == 1:
                break
        cases.append([gas, cost])
    short = [rng.randint(0, 1000) for _ in range(n)]
    cases.append([[max(0, c - 1) for c in short], short])
    return cases

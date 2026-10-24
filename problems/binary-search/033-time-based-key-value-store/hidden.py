def generate(rng):
    sets = 50000
    stamps = sorted(rng.sample(range(1, 10**7), sets))
    ops, params = ["TimeMap"], [[]]
    for t in stamps:
        ops.append("set")
        params.append(["key", "v" + str(t), t])
    for _ in range(100000 - 1 - sets):
        ops.append("get")
        params.append(["key", rng.randint(1, 10**7)])
    mixed_ops, mixed_params = ["TimeMap"], [[]]
    clock = {}
    for _ in range(99999):
        key = "k" + str(rng.randrange(5))
        if rng.random() < 0.5:
            clock[key] = clock.get(key, 0) + rng.randint(1, 100)
            mixed_ops.append("set")
            mixed_params.append([key, "x" + str(clock[key]), clock[key]])
        else:
            mixed_ops.append("get")
            mixed_params.append([key, rng.randint(1, max(clock.values(), default=1) + 50)])
    return [[ops, params], [mixed_ops, mixed_params]]

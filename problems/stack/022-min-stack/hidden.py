def generate(rng):
    ops, params = ["MinStack"], [[]]
    size = 0
    for i in range(100000 - 1):
        if size < 60000 and i < 60000:
            ops.append("push")
            params.append([rng.randint(-2**31, 2**31 - 1)])
            size += 1
            continue
        op = rng.choice(["getMin", "getMin", "top", "pop", "push"])
        if op == "pop" and size <= 1:
            op = "push"
        ops.append(op)
        if op == "push":
            params.append([rng.randint(-2**31, 2**31 - 1)])
            size += 1
        else:
            params.append([])
            size -= op == "pop"
    return [[ops, params]]

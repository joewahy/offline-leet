def generate(rng):
    cases = []
    for k in (3, 1000):
        nums = [rng.randint(-1000, 1000) for _ in range(50000)]
        ops, params = ["KthLargest"], [[k, nums]]
        for _ in range(50000):
            ops.append("add")
            params.append([rng.randint(-1000, 1000)])
        cases.append([ops, params])
    return cases

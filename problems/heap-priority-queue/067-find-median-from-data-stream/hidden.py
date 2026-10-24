def generate(rng):
    ops, params = ["MedianFinder"], [[]]
    for _ in range(50000):
        ops += ["addNum", "findMedian"]
        params += [[rng.randint(-100000, 100000)], []]
    ops.pop()
    params.pop()
    ascending = ["MedianFinder"]
    asc_params = [[]]
    for i in range(49999):
        ascending += ["addNum", "findMedian"]
        asc_params += [[i - 25000], []]
    return [[ops, params], [ascending, asc_params]]

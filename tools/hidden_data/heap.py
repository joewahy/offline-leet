HIDDEN = {
    61: ([
        ("`0 <= len(nums) <= 1000`, and the stream always has at least `k` values when `add` is called",
         "`0 <= len(nums) <= 10^5`, and the stream always has at least `k` values when `add` is called"),
        ("At most `1000` calls to `add`.", "At most `10^5` calls to `add`."),
    ], '''
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
'''),
    62: ([
        ("`1 <= len(stones) <= 1000`", "`1 <= len(stones) <= 10^5`"),
        ("`1 <= stones[i] <= 1000`", "`1 <= stones[i] <= 10^9`"),
    ], '''
def generate(rng):
    n = 100000
    return [
        [[rng.randint(1, 10**9) for _ in range(n)]],
        [[rng.randint(10**8, 10**9) for _ in range(n)]],
        [[rng.randint(1, 1000) for _ in range(n)]],
        [[1000] * n],
    ]
'''),
    67: ([("At most `10000` calls are made.", "At most `10^5` calls are made.")], '''
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
'''),
}

HIDDEN = {
    1: ([], '''
def generate(rng):
    n = 100000
    distinct = rng.sample(range(-10**9, 10**9), n)
    return [[distinct], [distinct[:-1] + [distinct[n // 2]]]]
'''),
    3: ([
        ("`2 <= len(nums) <= 1000`", "`2 <= len(nums) <= 10^5`"),
        ("`-10^4 <= nums[i] <= 10^4`", "`-10^9 <= nums[i] <= 10^9`"),
        ("`-10^4 <= target <= 10^4`", "`-10^9 <= target <= 10^9`"),
    ], '''
def generate(rng):
    n = 100000
    cases = []
    for _ in range(3):
        while True:
            nums = rng.sample(range(-10**9, 10**9), n)
            i, j = rng.sample(range(n), 2)
            target = nums[i] + nums[j]
            seen = set(nums)
            pairs = sum(1 for x in nums if target - x in seen and target - x != x) // 2
            if pairs == 1:
                break
        cases.append([nums, target])
    return cases
'''),
    7: ([("`2 <= len(nums) <= 10000`", "`2 <= len(nums) <= 10^5`")], '''
def generate(rng):
    n = 100000

    def signs():
        nums = [rng.choice((-1, 1)) for _ in range(n)]
        for i in rng.sample(range(n), 12):
            nums[i] = rng.choice((-2, 2, 3))
        return nums

    plain = signs()
    one_zero = signs()
    one_zero[rng.randrange(n)] = 0
    two_zeros = signs()
    a, b = rng.sample(range(n), 2)
    two_zeros[a] = two_zeros[b] = 0
    return [[plain], [one_zero], [two_zeros]]
'''),
    9: ([], '''
def generate(rng):
    n = 100000
    one_run = list(range(n))
    rng.shuffle(one_run)
    no_runs = [2 * v - 10**9 for v in range(n)]
    rng.shuffle(no_runs)
    pieces = []
    start = -10**9
    for length in (40000, 30000, 20000, 10000):
        pieces.extend(range(start, start + length))
        start += length + 5
    rng.shuffle(pieces)
    return [[one_run], [no_runs], [pieces]]
'''),
}

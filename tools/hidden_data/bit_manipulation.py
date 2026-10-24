HIDDEN = {
    144: ([("`1 <= len(nums) <= 9999` (always odd)", "`1 <= len(nums) <= 10^5` (always odd)")], '''
def generate(rng):
    cases = []
    for pairs in (49999, 30000):
        values = rng.sample(range(-30000, 30001), pairs + 1)
        nums = values[1:] * 2 + [values[0]]
        rng.shuffle(nums)
        cases.append([nums])
    return cases
'''),
    148: ([("`1 <= n <= 10000`", "`1 <= n <= 10^5`")], '''
def generate(rng):
    n = 100000
    cases = []
    for missing in (rng.randint(0, n), 0, n):
        nums = [v for v in range(n + 1) if v != missing]
        rng.shuffle(nums)
        cases.append([nums])
    return cases
'''),
}

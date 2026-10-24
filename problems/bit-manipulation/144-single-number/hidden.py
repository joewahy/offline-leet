def generate(rng):
    cases = []
    for pairs in (49999, 30000):
        values = rng.sample(range(-30000, 30001), pairs + 1)
        nums = values[1:] * 2 + [values[0]]
        rng.shuffle(nums)
        cases.append([nums])
    return cases

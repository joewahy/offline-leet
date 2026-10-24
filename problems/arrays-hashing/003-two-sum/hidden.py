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

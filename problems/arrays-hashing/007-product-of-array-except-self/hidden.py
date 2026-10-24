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

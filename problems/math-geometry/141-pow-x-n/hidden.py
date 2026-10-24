# The statement already allows the exponents used here, so its constraints are unchanged.
def generate(rng):
    return [
        [1.0000000001, 2**31 - 1],
        [0.9999999999, -2**31],
        [-1.0000000001, 2**31 - 1],
        [1.0, 2**31 - 1],
        [rng.uniform(1.0, 1.0000001), 2**31 - 7],
    ]

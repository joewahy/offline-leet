def generate(rng):
    n = 100000
    half = n // 2
    valley = [1000 - i * 1000 // half for i in range(half)] + [i * 1000 // half for i in range(half)]
    sawtooth = [(i % 2) * rng.randint(1, 1000) for i in range(n)]
    return [[[rng.randint(0, 1000) for _ in range(n)]], [valley], [sawtooth]]

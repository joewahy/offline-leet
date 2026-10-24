def generate(rng):
    cases = []
    for size, groups in ((1000, 100), (7, 14000), (1, 100000)):
        starts = rng.sample(range(0, 10**9, size + 1), groups)
        hand = [s + k for s in starts for k in range(size)]
        rng.shuffle(hand)
        cases.append([hand, size])
        broken = hand[:]
        broken[rng.randrange(len(broken))] += 1
        if size > 1:
            cases.append([broken, size])
    return cases

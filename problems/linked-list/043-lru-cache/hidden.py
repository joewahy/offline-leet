def generate(rng):
    def run(capacity, keys, hot=0):
        ops, params = ["LRUCache"], [[capacity]]
        filled = list(range(capacity)) if not hot else []
        rng.shuffle(filled)
        for key in filled:
            ops.append("put")
            params.append([key, rng.randint(0, 10**5)])
        for _ in range(99999 - len(filled)):
            key = rng.randrange(hot if hot and rng.random() < 0.8 else keys)
            if rng.random() < 0.5:
                ops.append("put")
                params.append([key, rng.randint(0, 10**5)])
            else:
                ops.append("get")
                params.append([key])
        return [ops, params]

    return [run(50000, 60000), run(5000, 20000, hot=3000)]

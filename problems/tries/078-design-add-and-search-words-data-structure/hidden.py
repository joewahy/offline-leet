def generate(rng):
    def word():
        return "".join(rng.choice("abcd") for _ in range(rng.randint(11, 13)))

    def with_dots(w, count):
        chars = list(w)
        for i in rng.sample(range(len(chars)), count):
            chars[i] = "."
        return "".join(chars)

    words = [word() for _ in range(30000)]
    ops, params = ["WordDictionary"], [[]]
    for w in words:
        ops.append("addWord")
        params.append([w])
    for _ in range(99999 - len(words)):
        base = rng.choice(words) if rng.random() < 0.6 else word()
        ops.append("search")
        params.append([with_dots(base, rng.randint(0, 2))])
    return [[ops, params]]

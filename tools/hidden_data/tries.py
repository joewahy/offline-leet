HIDDEN = {
    77: ([("At most `10000` calls are made.", "At most `10^5` calls are made.")], '''
def generate(rng):
    def word(alphabet, shortest, longest, prefix=""):
        return prefix + "".join(rng.choice(alphabet) for _ in range(rng.randint(shortest, longest)))

    def run(inserted, make):
        ops, params = ["PrefixTree"], [[]]
        for w in inserted:
            ops.append("insert")
            params.append([w])
        for _ in range(99999 - len(inserted)):
            w = rng.choice(inserted)
            kind = rng.choice(["search", "search_prefix", "starts", "starts_miss", "search_miss"])
            if kind == "search":
                ops.append("search")
                params.append([w])
            elif kind == "search_prefix":
                ops.append("search")
                params.append([w[: rng.randint(1, len(w) - 1)]])
            elif kind == "starts":
                ops.append("startsWith")
                params.append([w[: rng.randint(1, len(w))]])
            elif kind == "starts_miss":
                ops.append("startsWith")
                params.append([w + make()])
            else:
                ops.append("search")
                params.append([make()])
        return [ops, params]

    spread = [word("abcd", 8, 24) for _ in range(30000)]
    shared_prefix = "ab" * 50
    shared = [word("ab", 5, 10, shared_prefix) for _ in range(20000)]
    return [
        run(spread, lambda: word("abcd", 8, 24)),
        run(shared, lambda: word("ab", 5, 10, shared_prefix)),
    ]
'''),
    78: ([("At most `10000` calls are made, and at most 2 dots appear in any searched word.",
           "At most `10^5` calls are made, and at most 2 dots appear in any searched word.")], '''
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
'''),
}

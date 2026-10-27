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

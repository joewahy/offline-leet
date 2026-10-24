def generate(rng):
    pairs = {"(": ")", "[": "]", "{": "}"}
    opens = [rng.choice("([{") for _ in range(50000)]
    nested = "".join(opens) + "".join(pairs[c] for c in reversed(opens))
    broken = list(nested)
    broken[50000] = ")" if broken[50000] != ")" else "]"
    flat = "".join(rng.choice(["()", "[]", "{}"]) for _ in range(50000))
    return [[nested], ["".join(broken)], [flat]]

def check(args, got, expected, inputs):
    words = args[0]
    if not isinstance(got, str):
        return "return a string"
    if expected == "":
        return got == "" or "no valid order exists, expected an empty string"
    letters = {c for w in words for c in w}
    if len(got) != len(set(got)) or set(got) != letters:
        return "the result must contain each letter of the words exactly once"
    rank = {c: i for i, c in enumerate(got)}
    for a, b in zip(words, words[1:]):
        for x, y in zip(a, b):
            if x != y:
                if rank[x] > rank[y]:
                    return f"'{x}' must come before '{y}' because of the words {a!r} and {b!r}"
                break
    return True

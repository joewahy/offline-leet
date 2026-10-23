def check(args, got, expected, inputs):
    n, prereqs = args
    if not isinstance(got, list):
        return "return a list"
    if expected == []:
        return got == [] or "there is a cycle, so the answer must be an empty list"
    if sorted(got) != list(range(n)):
        return "the order must contain every course exactly once"
    pos = {c: i for i, c in enumerate(got)}
    for a, b in prereqs:
        if pos[b] > pos[a]:
            return f"course {b} must come before course {a}"
    return True

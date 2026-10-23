def _canon(items):
    return sorted(items, key=repr)


def matches(mode, got, expected):
    if mode == "exact":
        return got == expected
    if not isinstance(got, list):
        return False
    if mode == "unordered":
        return _canon(got) == _canon(expected)
    if mode == "unordered_nested":
        if not all(isinstance(g, list) for g in got):
            return False
        return _canon(_canon(g) for g in got) == _canon(_canon(e) for e in expected)
    raise ValueError(f"unknown compare mode {mode!r}")

import json
import math


def norm(value):
    """Round-trip through JSON so tuples become lists and objects become reprs."""
    return json.loads(json.dumps(value, default=repr))


def same(a, b):
    """Equality that does not let True == 1 slip through."""
    if isinstance(a, bool) or isinstance(b, bool):
        return type(a) is type(b) and a == b
    if isinstance(a, list) and isinstance(b, list):
        return len(a) == len(b) and all(same(x, y) for x, y in zip(a, b))
    if isinstance(a, dict) and isinstance(b, dict):
        return a.keys() == b.keys() and all(same(a[k], b[k]) for k in a)
    return a == b


def _canon(items):
    return sorted(items, key=repr)


def matches(mode, got, expected):
    if mode == "exact":
        return same(got, expected)
    if mode == "float":
        return (
            isinstance(got, (int, float))
            and not isinstance(got, bool)
            and math.isclose(got, expected, rel_tol=1e-5, abs_tol=1e-5)
        )
    if not isinstance(got, list):
        return False
    if mode == "unordered":
        return _canon(got) == _canon(expected)
    if mode == "unordered_outer":
        # outer order is free, each inner list must match exactly
        return _canon(got) == _canon(expected)
    if mode == "unordered_nested":
        if not all(isinstance(g, list) for g in got):
            return False
        return _canon(_canon(g) for g in got) == _canon(_canon(e) for e in expected)
    raise ValueError(f"unknown compare mode {mode!r}")

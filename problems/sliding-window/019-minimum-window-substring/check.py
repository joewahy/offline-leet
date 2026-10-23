from collections import Counter


def check(args, got, expected, inputs):
    s, t = args
    if not isinstance(got, str):
        return "return a string"
    if expected == "":
        return got == "" or "no valid window exists, expected an empty string"
    if len(got) != len(expected):
        return f"window length {len(got)} is not the minimum ({len(expected)})"
    if got not in s:
        return "result is not a substring of s"
    if Counter(t) - Counter(got):
        return "result does not contain every character of t"
    return True

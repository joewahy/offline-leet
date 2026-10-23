def check(args, got, expected, inputs):
    s = args[0]
    if not isinstance(got, str):
        return "return a string"
    if got not in s:
        return "result is not a substring of s"
    if got != got[::-1]:
        return "result is not a palindrome"
    if len(got) != len(expected):
        return f"a palindrome of length {len(expected)} exists, yours has length {len(got)}"
    return True

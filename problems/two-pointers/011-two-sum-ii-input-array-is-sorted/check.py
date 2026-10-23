def check(args, got, expected, inputs):
    nums, target = args
    ok = isinstance(got, list) and len(got) == 2 and all(type(x) is int for x in got)
    if not ok:
        return "return a list of two integer positions"
    i, j = got
    if not 1 <= i < j <= len(nums):
        return "positions must be 1-based with i < j"
    if nums[i - 1] + nums[j - 1] != target:
        return f"numbers[{i}] + numbers[{j}] = {nums[i - 1] + nums[j - 1]}, not {target}"
    return True

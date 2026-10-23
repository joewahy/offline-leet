def check(args, got, expected, inputs):
    gas, cost = args
    if type(got) is not int:
        return "return an integer index"
    if expected == -1:
        return got == -1 or "no starting station works, expected -1"
    if not 0 <= got < len(gas):
        return "the index is out of range"
    tank = 0
    for k in range(len(gas)):
        i = (got + k) % len(gas)
        tank += gas[i] - cost[i]
        if tank < 0:
            return f"you run out of fuel before station {(i + 1) % len(gas)} when starting at {got}"
    return True

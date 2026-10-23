from leet.structures import graph_to


def check(args, got, expected, inputs):
    originals = set()
    stack = [inputs[0]] if inputs[0] is not None else []
    while stack:
        node = stack.pop()
        if id(node) not in originals:
            originals.add(id(node))
            stack.extend(node.neighbors)
    if graph_to(inputs[0]) != args[0]:
        return "the original graph was modified"
    if graph_to(got) != args[0]:
        return "the clone does not have the same values and connections as the original"
    stack, seen = ([got] if got is not None else []), set()
    while stack:
        node = stack.pop()
        if id(node) in seen:
            continue
        seen.add(id(node))
        if id(node) in originals:
            return "the clone reuses nodes of the original graph"
        stack.extend(node.neighbors)
    return True

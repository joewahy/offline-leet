from leet.structures import random_to


def check(args, got, expected, inputs):
    original = inputs[0]
    ids = set()
    node = original
    while node is not None:
        ids.add(id(node))
        node = node.next
    if random_to(original) != args[0]:
        return "the original list was modified"
    if random_to(got) != args[0]:
        return "the copy does not have the same values and pointers as the original"
    node = got
    while node is not None:
        if id(node) in ids or (node.random is not None and id(node.random) in ids):
            return "the copy reuses nodes of the original list"
        node = node.next
    return True

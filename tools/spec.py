"""Helpers for writing problem specs. See tools/build.py."""


def P(id, title, difficulty, method, statement, stub, reference, cases, **opts):
    """One problem.

    statement  markdown body (Examples / Constraints / Hints sections)
    stub       starter code shown to the user
    reference  a correct solution; also generates expected values for `gen`
    cases      hand-written [args, expected] pairs; expected is derived by hand,
               so they independently check the reference
    opts       gen(rng) -> list of extra args (expected comes from the reference)
               small(rng) -> args + brute (source): cross-check reference vs brute force
               checker (source of check.py), compare, arg_types, return_type,
               inplace, design, roundtrip, timeout
    """
    return dict(
        id=id, title=title, difficulty=difficulty, method=method, statement=statement,
        stub=stub, reference=reference, cases=cases, **opts,
    )


LIST_HDR = """# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""

TREE_HDR = """# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""

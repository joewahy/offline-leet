# 41. Add Two Numbers (Medium)

Two non-negative integers are stored in two linked lists, one digit per node, with the least significant digit first. For example `342` is stored as `[2, 4, 3]`.

Add the two numbers and return the sum as a linked list in the same format.

## Examples

```
Input:  l1 = [2, 4, 3], l2 = [5, 6, 4]
Output: [7, 0, 8]          # 342 + 465 = 807

Input:  l1 = [9, 9], l2 = [1]
Output: [0, 0, 1]          # 99 + 1 = 100
```

## Constraints

- `1 <= number of nodes in each list <= 3000`
- `0 <= node.val <= 9`
- No list has leading zeros, except the number `0` itself.

<details>
<summary>Hints (spoilers: open one at a time)</summary>

1. The digits are stored with the least significant digit first, which is the order you add in on paper.
2. Walk both lists together, adding the two digits plus a carry, and build the result list as you go.
3. At each step `total = a + b + carry`; append `total % 10` and carry `total // 10`. Keep going while either list has nodes or the carry is nonzero. A dummy head node simplifies building the result.

</details>

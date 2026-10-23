from collections import Counter


class Solution:
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize:
            return False
        count = Counter(hand)
        for x in sorted(count):
            need = count[x]
            if need:
                for y in range(x, x + groupSize):
                    if count[y] < need:
                        return False
                    count[y] -= need
        return True

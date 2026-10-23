class Solution:
    def carFleet(self, target, position, speed):
        fleets = 0
        slowest = 0.0
        for p, s in sorted(zip(position, speed), reverse=True):
            t = (target - p) / s
            if t > slowest:
                fleets += 1
                slowest = t
        return fleets

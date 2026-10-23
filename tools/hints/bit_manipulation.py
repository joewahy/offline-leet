HINTS = {
    149: [
        "Think about how you add in binary. Which operation gives the sum without carries, and which gives the carries?",
        "XOR adds without carrying. AND, shifted left by one, gives the carry.",
        "Repeat `a, b = a ^ b, (a & b) << 1` until `b` is 0. In Python, integers are unbounded, so mask to 32 bits (`& 0xFFFFFFFF`) at each step, and convert back to a negative number at the end if the 32nd bit is set.",
    ],
    150: [
        "Peel off the last digit with `% 10` and add it to the end of a new number.",
        "Handle the sign separately: work with the absolute value, then put the sign back.",
        "Build `rev = rev * 10 + digit` while dividing the input by 10. In Python nothing overflows by itself, so check at the end whether the result is within `[-2^31, 2^31 - 1]` and return `0` if it is not.",
    ],
}

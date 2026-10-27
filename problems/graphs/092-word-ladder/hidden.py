def generate(rng):
    def words_over(alphabet, length, count):
        words = set()
        while len(words) < count:
            words.add("".join(rng.choice(alphabet) for _ in range(length)))
        return sorted(words)

    def ladder(alphabet, length, count, reachable):
        words = words_over(alphabet, length, count)
        rng.shuffle(words)
        begin = words.pop()
        end = words[0] if reachable else "".join(rng.choice(alphabet) for _ in range(length))
        return [begin, end, words]

    return [
        ladder("abcde", 8, 40000, True),
        ladder("abc", 10, 30000, True),
        ladder("abcde", 8, 40000, False),
    ]
